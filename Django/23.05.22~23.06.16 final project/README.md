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