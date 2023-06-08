# 23.05.22
* 지금 까지의 조 분위기는 가장 좋았다.
* 커플매칭의 주제와 추가적인 기능에 찾지만 뭐가 좋을지 좋은 생각은 없지만 계속 생각을 해봐야겠다.

# 23.05.23
* 분위기 최고 제일 재밌다.
* 갑자기 음악에 빠져서 다같이 좋아하는 노래 듣고 놀음... 내일은 확실하게 진행하자 ㅋㅋ

# 23.05.24
* 지금 코드가 나에게 없다... 통제 당한다.. ㅋㅋㅋ 하지만 온르은 많은 이야기와 ERD구성등등 시작했다. 프론트를 위한 뼈대 작성을 조금있다 조금하다 자야지..

# 23.05.25
* 아 작업하다 커밋하는거 또 까먹었다 ㅂㄷㅂㄷㅂㄷㅂㄷ...
* 오늘은 분업으로 나는 음원 api를 구현했다.
profile에 spotify api를 받아와서 음원 검색 => 리스트 출력 => 재생 => 재생버튼 누른 음원을 남기고 나머지 음원 사라짐 까지는 구현 했지만
남은 음원을 db에 저장하려 했지만 search한 모든 데이터가 다 들어간다 이 부분은 내일 한번 다른 분들과 의논해보고 수정해야겠다.

# 23.05.26
* 오늘은 시작부터 끝까지 spotify api로 받아온 데이터를 db에 저장하는 views.py를 계속 수정했다

```python

tracks = {}
def search_spotify(request):
    global tracks
    if request.method == 'GET':
        query = request.GET.get('q')

        if query:
            tracks = search(query)  # 검색 기능 사용
            context = {
                'tracks': tracks,
            }
            return render(request, 'accounts/profile.html', context)
        return render(request, 'accounts/profile.html')



def save_track(request):
    global tracks
    if request.method == 'POST':
        selected_tracks = request.POST.getlist('selected_tracks[]')
    music = Track.objects.filter(user_id=request.user.id)
    if music is not None:
        music.delete()
    
    for track_id in selected_tracks:
        for track in tracks:
            if track_id == track['id']:
                Track.objects.create(
                    title=track['name'],
                    artist=track['artists'][0]['name'],
                    album=track['album']['name'],
                    image_url=track['album']['images'][0]['url'],
                    preview_url=track['preview_url'],
                    user = request.user
                )
        return redirect('accounts:profile', username=request.user.username)
    else:
        return HttpResponseBadRequest("Invalid request method.")
```

search_spotify에서 json의 데이터를 민지님의 도움으로 분석했고 save_track 에 global을 통해 정환님과 함께 user에 대한 profile music를 db에 저장하는대 까지 성공했다. 역시 백엔드가 막힐때는 답답하지만 문제를 해결하면 재미는 더 있는거 같다. 오늘은 금요일이고 첫 주말이기도 하니 일단 좀 쉬자는 이야기가 나왔지만 주말에 약속이 없다면 혼자 할 것도 한번 생각해 봐야겠다.


# 23.05.28~29
토요일은 휴식!! 그리고 28일 저녁부터 오늘까지 profile music 기능을 다듬었다.
체크박스가 하나만 클릭되도록 / 체크박스를 클릭하면 해당 음원을 제외하고 나머지 리스트 숨김 / 체크박스를 체크하지 않으면 저장버튼 비활성화 => 추가로 비활성화된 저장 버튼을 누르면 에러메시지가 나오도록 하고 싶은데 아직 미구현 내일 팀원들에게 물어보고 어떻게 구현할지 정함/ 모달창에서 나와서 저장한 음원데이터를 profile_main페이지에서 이미지까지 출력되도록 구현 등등 어제 오늘 진행한 내용이다.

# 23.05.30 ~ 31
30,31일 가능한 오류도 잡고 더이상 spotify api쪽 기능에 프론트제외 기능 구현은 완성한 기분이다. posts앱의 create와 save_track을 합쳐서 posts의 create가 작성됨과 동시에 음원이 db에 저장이 되도록 그리고 음원이 없을때 있을때를 구분 따로 가져와서 출력할 수 있도록 최대한 생각나는 부분은 출력해서 프론트에게 넘겨준거같다. 큰 산은 넘긴 기분? 앞으로 어떤 기능을 할지 모르지만 깔끔히 작성하고 싶다.

# 23.06.01 ~ 02
어제 늦개까지 작업해서 작성 못함;; 어제 오늘 spotify 관련 해서 update 작업이랑 익명게시판을 만들면서 에브리타임을 바탕으로 만들려고 했지만 실패했다..
오늘은 하루종일 update에서 instance=comment 값이 넘어오지 않아서 작업하다가 결국 지수님의 도움으로 해결했다 detail을 의심은 했지만 왜 더 파고들어서 작업을 안했을까..
아무튼 지수님의 도움으로 해결한 코드이다

```python
def anonymous_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = CommentForm()
    comments = post.comments.all()
    comment_forms = []
    for comment in comments:
        u_comment_form = (
            comment,
            CommentForm(instance=comment)
        )
        comment_forms.append(u_comment_form) 
    tags = post.tags.all()
    posts = Post.objects.exclude(user=request.user).order_by('like_users')
    music = PostTrack.objects.filter(post=post_pk)
    context ={
        'post' : post,
        'comment_forms': comment_forms,
        'comment_form': comment_form,
        'comments' : comments,
        'tags' : tags,
        'posts' : posts,
        'music' : music,
    }

    # Generate or retrieve anonymous ID for the current user
    anonymous_id = request.session.get('anonymous_id')
    if not anonymous_id:
        anonymous_id = generate_anonymous_id()
        request.session['anonymous_id'] = anonymous_id
    context['anonymous_id'] = anonymous_id
    
    return render(request, 'posts/anonymous_detail.html', context)
```
    앞으로는 의심을 했으면 조금더 파고들어야겠다...

# 23.06.07
휴일 4일동안 별다른 코딩은 조금만 해서 별다른 내용은 없다 휴일에서 가져온 문제를 오늘 하루종일 했지만 해결을 못했는대 페이지 네이션을 사용했을때 ajax로 데이터를 받아오면 자꾸 페이지 네이션이 안되거나 ajax가 안되거나 또는 페이지가 두번 출력되는 현상이 계속 발생한다 JS를 사용을 잘 못해서 답답한게 너무 크다.

# 23.06.08
결국 페이지 네이션 버튼을 바꿔서 ajax를 적용하는대 성공했다
```html
  $(document).ready(function() {
    // 드롭다운 선택 이벤트 리스너
    $('#section-dropdown').on('change', function() {
      var selectedSection = $(this).val();
      var currentPage = 1; // 첫 페이지로 설정
      var url = '{% url 'posts:index' %}';
      // AJAX 요청 전송
      sendAjaxRequest(url, selectedSection, currentPage);
    });
  
    // 페이지 번호 클릭 이벤트 리스너
    $(document).on('click', '.page-link', function(event) {
      event.preventDefault();
      var selectedPage = $(this).attr('href').split('=')[1];
      var selectedSection = $('#section-dropdown').val();
      var url = '{% url 'posts:index' %}';
      // AJAX 요청 전송
      sendAjaxRequest(url, selectedSection, selectedPage);
    });
  
    // 첫 페이지 클릭 이벤트 리스너
    $(document).on('click', '.first-page', function() {
      var selectedSection = $('#section-dropdown').val();
      var url = '{% url 'posts:index' %}';
      // AJAX 요청 전송
      sendAjaxRequest(url, selectedSection, 1);
    });
  
    // AJAX 요청 전송 함수
    function sendAjaxRequest(url, section, page) {
      $.ajax({
        url: url,
        method: 'GET',
        data: { section: section, page: page },
        success: function(response) {
          // 서버로부터 받은 HTML을 section-posts 영역에 대체
          $('#section-posts').html($(response).find('#section-posts').html());
          // 선택된 섹션을 유지하기 위해 드롭다운 값을 설정
          $('#section-dropdown').val(section);
          // 현재 페이지 데이터 속성 업데이트
          $('#section-posts').data('current-page', page);
          updatePagination(); // 페이지네이션 업데이트
        }
      });
    }
  
    // 페이지네이션 업데이트 함수
    function updatePagination() {
      var currentPage = parseInt($('#section-posts').data('current-page')) || 1;
      var total_pages = parseInt('{{ total_pages }}') || 1;
      var pageLinks = $('.page-link');
      pageLinks.parent('.page-item').removeClass('active');
  
      // 현재 페이지 버튼에 active 클래스 추가
      pageLinks.each(function() {
        var pageNumber = $(this).attr('href').split('=')[1];
        if (pageNumber == currentPage) {
          $(this).parent('.page-item').addClass('active');
        }
      });
  
      // 페이지 범위 설정
      var pageRange = 5; // 출력할 페이지 범위 크기
      var startPage = Math.max(1, currentPage - Math.floor(pageRange / 2));
      var endPage = Math.min(total_pages, startPage + pageRange - 1);
      startPage = Math.max(1, endPage - pageRange + 1);
  
      // 페이지 버튼 업데이트
      var paginationContainer = $('.pagination');
      paginationContainer.empty();
  
      // 첫 페이지와 이전 페이지 버튼
      if (currentPage > 1) {
        paginationContainer.append('<li class="page-item first-page"><a class="page-link" href="?page=1">처음</a></li>');
        paginationContainer.append('<li class="page-item previous-page"><a class="page-link" href="?page=' + (currentPage - 1) + '">이전</a></li>');
      }
  
      // 페이지 버튼
      for (var i = startPage; i <= endPage; i++) {
        if (i == currentPage) {
          paginationContainer.append('<li class="page-item active"><a class="page-link" href="?page=' + i + '">' + i + '</a></li>');
        } else {
          paginationContainer.append('<li class="page-item"><a class="page-link" href="?page=' + i + '">' + i + '</a></li>');
        }
      }
  
      // 다음 페이지와 마지막 페이지 버튼
      if (currentPage < total_pages) {
        paginationContainer.append('<li class="page-item next-page"><a class="page-link" href="?page=' + (currentPage + 1) + '">다음</a></li>');
        paginationContainer.append('<li class="page-item last-page"><a class="page-link" href="?page=' + total_pages + '">마지막</a></li>');
      }
    }
  });
```
내가짠 코드는 아니지만 많은 시간을 들여서 성공했다 추가로 댓글에 필터걸고 지금 현제 더보기 버튼을 누르면 댓글이 5개씩 보일 수 있도록 도전 중이다
오늘 컨디션이 별루여서 힘들었지만 조금 쉬다가 가서 완성시키고 자는게 목표다.