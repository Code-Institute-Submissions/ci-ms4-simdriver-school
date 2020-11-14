from django import forms
from .models import Week, Datapack, RaceTrack


class DatapackForm(forms.ModelForm):

    class Meta:
        model = Datapack
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        weeks = Week.objects.all()
        week_friendly_names = [(w.id, w.get_friendly_name()) for w in weeks]

        race_tracks = RaceTrack.objects.all()
        tracks_friendly_names = [
            (r.id, r.get_friendly_name()) for r in race_tracks
            ]

        self.fields['week'].choices = week_friendly_names
        self.fields['track_name'].choices = tracks_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
