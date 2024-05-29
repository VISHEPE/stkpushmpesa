In this example, the stk_push function is used to make the STK Push request using mpesa payment getway/api.
The function takes a single argument, which is the STK Push payload. 
The payload is a dictionary that contains all the necessary information for the STK Push request, such as the business short code,
the amount, the phone number, and the callback URL.

The make_stk_push function returns a dictionary that contains 
the response from the M-Pesa API. In this example, the response is returned as an HTTP response.
