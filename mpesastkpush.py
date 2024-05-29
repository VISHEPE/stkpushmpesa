from mpesa.views import stk_push

def stk_push_view(request):
    # Define the STK Push payload
    payload = {
        'BusinessShortCode': 8860790,
        'Password': 12234455566,
        'Timestamp': generate_timestamp(),
        'TransactionType': 'CustomerPayBillOnline',
        'Amount': '100',
        'PartyA': '254722000000',
        'PartyB': 434556667,
        'PhoneNumber': '254745135328',
        'CallBackURL': 'https://vishepe/callback/',
        'AccountReference': 'Test Account',
        'TransactionDesc': 'Test Transaction'
    }

    # Make the STK Push request
    response = stk_push(payload)

    # Do something with the response
    return HttpResponse(json.dumps(response), content_type='application/json')