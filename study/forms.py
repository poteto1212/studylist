from django import forms
from .models import SubjectList,SubSubjectList,Studylist

#絞り込み機能の実装
class SelectSubjectForm(forms.ModelForm):
    #親カテゴリによる絞り込みの為に定義する
    parent_subjectlist=forms.ModelChoiceField(
        label='科目選択',
        queryset=SubjectList.objects.all(),
        required=False,
        )
        
    class Meta:
        model=SubSubjectList
        fields='__all__'
    
    fields_order=('parent_subjectlist','subjectlist')
    
        
        