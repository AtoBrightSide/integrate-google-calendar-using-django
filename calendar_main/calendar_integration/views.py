from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View
import requests

class GoogleCalendarInitView(View):
    def get(self, request):
        # Set the necessary parameters for the OAuth process
        client_id = settings.CLIENT_ID
        redirect_uri = settings.REDIRECT_URI
        print(f"client id is -> {client_id}\nredirect uri -> {redirect_uri}")
        scope = 'https://www.googleapis.com/auth/calendar'
        
        # Redirect the user to the Google authorization endpoint
        auth_url = f'https://accounts.google.com/o/oauth2/auth?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&response_type=code'
        return redirect(auth_url)

class GoogleCalendarRedirectView(View):
    def get(self, request):
        # Make a POST request to the Google token endpoint to exchange the authorization code for an access token
        response = requests.post(
            'https://accounts.google.com/o/oauth2/token',
            data={
                'client_id': settings.CLIENT_ID,
                'client_secret': settings.CLIENT_SECRET,
                'redirect_uri': settings.REDIRECT_URI,
                'code': request.GET.get('code'),
                'grant_type': 'authorization_code',
            }
        )
        
        # Parse the response to retrieve the access token
        access_token = response.json().get('access_token')
        
        calendar_id = 'primary'
        
        # Make a GET request to the Google Calendar API to retrieve a list of events
        response = requests.get(
            f'https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events',
            headers={
                'Authorization': f'Bearer {access_token}',
            }
        )
        print(response.json())
        # Parse the response to retrieve the list of events
        events = response.json().get('items', [])
        
        # Return the list of events as a JSON response
        return JsonResponse(events, safe=False)
