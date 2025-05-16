from rest_framework import serializers
from .models import Language, TextChallenge, ChallengeAttempt

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language                                                                                           
        fields = ['language_code', 'language_name', 'is_active']                                               
 
class TextChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextChallenge
        fields = [
            'challenge_id',        
            'difficulty_level',    
            'language',            
            'recommended_time',    
            'content',             
            'word_count',          
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['language'] = instance.language.language_code
        
        return representation


# hereglegchiin oroldlogo buyu tuuh
class ChallengeAttemptSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)      # Нэмэлтээр user.username-ыг харуулах (бараг virtual field мэт)
    challenge_difficulty = serializers.CharField(source='challenge.difficulty_level', read_only=True)  # Нэмэлтээр challenge.difficulty_level-ыг харуулах
    language = serializers.CharField(source='challenge.language.language_name', read_only=True) #ymr hel deer shivsenee xarna

    class Meta:
        model = ChallengeAttempt
        
        fields = [
            'id',                    # Оролцоо ID
            'user',                  # Хэн оролцсон (FK)
            'username',              # Хэрэглэгчийн нэр (read_only)
            'challenge',             # Ямар сорилд оролцсон (FK)
            'challenge_difficulty',  # Сорилын түвшин (read_only)
            'language',              # ymr hel deer shivsenee haruulna
            'correct_word_count',    # Зөв бичсэн үгийн тоо
            'wrong_word_count',      # Буруу бичсэн үгийн тоо
            'duration_seconds',      # Сорилд зарцуулсан хугацаа (секунд)
            'created_at',            # Бүртгэгдсэн огноо (автоматаар нэмэгдэнэ)
        ]
        
        read_only_fields = ['created_at', 'user']
