# N:1 Relation
## GET - List
* 댓글 데이터 목록 조회하기
```python
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # 유효성 검사에서는 제외시키고, 데이터 조회시에는 제공 (읽기 전용 속성)
        read_only_fields = ('article',)

path('comments/', views.comment_list),

@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many= True)
    return Response(serializer.data)
```
## GET - Detail
* 단일 댓글 데이터 조회하기
```python
path('comments/<int:comment_pk>/',views.comment_detail),

@api_view(['GET'])
def comment_detail(request,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)
```

## POST
* 단일 댓글 데이터 생성하기
```python
path('articles/<int:article_pk>/comments/',views.comment_create),

@api_view(['POST'])
def comment_create(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = CommentSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```
* save()메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음
* CommentSerializer를 통해 Serialize되는 과정에서 Parameter로 넘어온 article_pk에 해당하는 article객체를 추가적인 데이터를 넘겨 저장

### 읽기 전용 필드 설정
* **read_only_fields**를 사용해 외래 키 필드를 '읽기 전용 필드' 로 설정
* 읽기 전용 필드는 데이터를 전송하는 시점에 **'해당 필드를 유효성 검사에서 제외시키고, 데이터 조회 시에는 출력'**하도록 함

# N:1 - 역참조 데이터 조회

## 2가지 역참조 상황 작성해보기
1. 특정 게시글에 작성된 댓글 목록 출력하기
  * 기존필드 override
    1. PrimarykeyRelatedField()
    2. Nested relationships

2. 특성 게시글에 작성된 댓글의 개수 출력하기
  * 새로운 필드 추가


## 특정 게시글에 작성된 댓글 목록 출력하기
1. PrimarykeyRelatedField()
  * 게시글 조회 시 해당 게시글의 댓글 목록까지 함께 출력하기
  * Serializer는 기존 필드를 override 하거나 추가적인 필드를 구성할 수 있음

```python
class ArticleSerializer(serializers.ModelSerializer):

    class MyCommentSerializer(serializers.ModelSerializer):
     class Meta:
        model = Comment
        fields = ('id','content',)

    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    comment_set = MyCommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
```
2. Nested relationships
  * 모델관계 상으로 참조 된 대상은 참조하는 대상의 표현에 포함되거나 중첩(nested)될 수 있음
  * 이러한 중첩된 관계는 serializer를 필드로 사용하여 표현 가능

  * source
    * 필드를 채우는 데 사용할 속성의 이름
    * 점 표기법(dotted notation)을 사용하여 속성을 탐색 할 수 있음
    

