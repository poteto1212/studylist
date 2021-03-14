from django.db import models

class SubjectList(models.Model):
    subjectlist=models.CharField(verbose_name='科目一覧',max_length=30)
    
    def __str__(self):
        return self.subjectlist
    
class Studylist(models.Model):
    subjectlist=models.ForeignKey(
        SubjectList,
        verbose_name='科目',
        on_delete=models.CASCADE
        )
    
    problem=models.CharField(
        verbose_name='問題',
        max_length=500
        )
    
    answer=models.CharField(
        verbose_name='答え',
        max_length=500
        )
    
    detail=models.TextField(
        verbose_name='詳しい説明',
        max_length=1000,
        default='ここに解説を入力してください',
        )
        
    def __str__(self):
        return str(self.subjectlist)
