from rest_framework import serializers
from .models import Comment, Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Review
        fields = ('id', 'author', 'pub_date', 'score', 'text')
        read_only_fields = ('id', 'author')

    def validate_score(self, value):
        if (0 <= value < 10):
            raise serializers.ValidationError('Введите оценку от 1 до 10')
        return value

    def validate(self, data):
        if Review.objects.filter(
                title=self.context['view'].kwargs['title_id'],
                author=self.context['request'].user
        ).exists() and self.context['request'].method == 'POST':
            raise serializers.ValidationError(
                'Вы уже оставляли здесь отзыв!')
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'pub_date', 'text')
