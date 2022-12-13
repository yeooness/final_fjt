from django.forms import ModelForm, DateInput
from calendarapp.models import Event, Dogwalking_Journal, EventMember
from django import forms


class EventForm(ModelForm):
    class Meta:
        model = Event
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
            "start_time": DateInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
            # "end_time": DateInput(
            #     attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            # ),
        }
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
        # self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)


class DailyEventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            "journal_board",
            "content",
            "image",
            "start_time",
        ]
        labels = {
            "journal_board": "작성할 일기",
            "content": "내용",
            "image": "사진",
            "start_time": "날짜",
        }
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
            "start_time": DateInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
            # "end_time": DateInput(
            #     attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            # ),
        }
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(DailyEventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
        # self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)


class DogwalkingEventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            "route",
            "consumed_calories",
            "walking_time",
            "start_time",
        ]
        labels = {
            "route": "산책 경로",
            "consumed_calories": "소모된 칼로리",
            "walking_time": "소요된 시간",
            "start_time": "산책한 시간",
        }
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
            "start_time": DateInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
            # "end_time": DateInput(
            #     attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            # ),
        }
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(DailyEventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
        # self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)


class HealthEventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            "meals",
            "energy",
            "medicine",
            "start_time",
        ]
        labels = {
            "meals": "급여",
            "energy": "활력",
            "medicine": "약",
            "start_time": "급여/약 시간",
        }
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
            "start_time": DateInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
            # "end_time": DateInput(
            #     attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            # ),
        }
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(DailyEventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
        # self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)


class DogwalkingJournalForm(ModelForm):
    class Meta:
        model = Dogwalking_Journal
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
            "start_time": DateInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
        }
        exclude = ["user"]
        fields = [
            "route",
            "consumed_calories",
            "walking_time",
            "start_time",
        ]
        labels = {
            "route": "산책 경로",
            "consumed_calories": "소모된 칼로리",
            "walking_time": "소요된 시간",
            "start_time": "산책한 날짜",
        }

    def __init__(self, *args, **kwargs):
        super(DogwalkingJournalForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = EventMember
        fields = ["user"]
