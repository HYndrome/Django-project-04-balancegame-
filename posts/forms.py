from django import forms
from .models import Post
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill

class PostForm(forms.ModelForm):
    image1 = ProcessedImageField(
        spec_id='posts:image1',
        processors=[ResizeToFill(200,200)],
        format='JPEG',
        options={'quality' : 50},
        required=False,
    )

    image2 = ProcessedImageField(
        spec_id='posts:image2',
        processors=[ResizeToFill(200,200)],
        format='JPEG',
        options={'quality' : 50},
        required=False,
    )

    class Meta:
        model = Post
        fields = ('title', 'select1_content', 'image1', 'select2_content', 'image2', )