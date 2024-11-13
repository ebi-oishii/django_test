from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    """ログイン画面用のフォーム"""
    username = forms.CharField(label="ユーザー名", max_length=255)
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data["username"]
        if len(username) < 3:
            raise forms.ValidationError("%(min_length)s文字以上で入力してください", code="invalid", params={"min_length": 3})
        return username
    
    def clead(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("正しいユーザー名を入力してください")
        
        if not user.check_password(password):
            raise forms.ValidationError("正しいパスワードを入力してください")
        

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        widgets = {"password": forms.PasswordInput(attrs={"placeholder": "パスワード"})}

    password2 = forms.CharField(label="確認用パスワード", required=True, widget=forms.PasswordInput(attrs={"placeholder": "確認用パスワード"}))

    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        self.fields["username"].widget.attrs = {"placeholder": "ユーザー名"}
        self.fields["email"].required = True
        self.fields["email"].widget.attrs = {"placeholder": "メールアドレス"}


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email", "profile_image")

