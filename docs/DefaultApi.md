# woolworths.DefaultApi

All URIs are relative to *https://www.woolworths.com.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_ui_v2_bootstrap_get**](DefaultApi.md#api_ui_v2_bootstrap_get) | **GET** /api/ui/v2/bootstrap | GET bootstrap
[**api_v3_ui_authentication_otp_post**](DefaultApi.md#api_v3_ui_authentication_otp_post) | **POST** /api/v3/ui/authentication/otp | POST otp
[**api_v3_ui_checkout_digitalpay_instruments_get**](DefaultApi.md#api_v3_ui_checkout_digitalpay_instruments_get) | **GET** /api/v3/ui/checkout/digitalpay/instruments | GET instruments
[**api_v3_ui_fulfilment_feestructure_id_get**](DefaultApi.md#api_v3_ui_fulfilment_feestructure_id_get) | **GET** /api/v3/ui/fulfilment/feestructure/{id} | GET feestructure by id
[**api_v3_ui_fulfilment_windows_get**](DefaultApi.md#api_v3_ui_fulfilment_windows_get) | **GET** /api/v3/ui/fulfilment/windows | GET windows
[**api_v3_ui_mylists_get**](DefaultApi.md#api_v3_ui_mylists_get) | **GET** /api/v3/ui/mylists | GET mylists
[**api_v3_ui_order_amending_get**](DefaultApi.md#api_v3_ui_order_amending_get) | **GET** /api/v3/ui/order/amending | GET amending
[**api_v3_ui_packaging_preferences_get**](DefaultApi.md#api_v3_ui_packaging_preferences_get) | **GET** /api/v3/ui/PackagingPreferences | GET packagingpreferences
[**api_v3_ui_packaging_preferences_id_post**](DefaultApi.md#api_v3_ui_packaging_preferences_id_post) | **POST** /api/v3/ui/PackagingPreferences/{id} | POST packagingpreferences by id
[**api_v3_ui_trolley_update_post**](DefaultApi.md#api_v3_ui_trolley_update_post) | **POST** /api/v3/ui/trolley/update | POST trolley update
[**apis_ui_checkout_confirm_order_get**](DefaultApi.md#apis_ui_checkout_confirm_order_get) | **GET** /apis/ui/Checkout/ConfirmOrder | GET confirmorder
[**apis_ui_checkout_digital_pay_initialize_credit_card_iframe_post**](DefaultApi.md#apis_ui_checkout_digital_pay_initialize_credit_card_iframe_post) | **POST** /apis/ui/Checkout/DigitalPay/InitializeCreditCardIframe | POST initializecreditcardiframe
[**apis_ui_checkout_digital_pay_payment_post**](DefaultApi.md#apis_ui_checkout_digital_pay_payment_post) | **POST** /apis/ui/Checkout/DigitalPay/Payment | POST payment
[**apis_ui_checkout_get**](DefaultApi.md#apis_ui_checkout_get) | **GET** /apis/ui/Checkout | GET checkout
[**apis_ui_delivery_delivery_info_get**](DefaultApi.md#apis_ui_delivery_delivery_info_get) | **GET** /apis/ui/Delivery/DeliveryInfo | GET deliveryinfo
[**apis_ui_delivery_options_get**](DefaultApi.md#apis_ui_delivery_options_get) | **GET** /apis/ui/Delivery/Options | GET options
[**apis_ui_delivery_options_post**](DefaultApi.md#apis_ui_delivery_options_post) | **POST** /apis/ui/Delivery/Options | POST options
[**apis_ui_fulfilment_post**](DefaultApi.md#apis_ui_fulfilment_post) | **POST** /apis/ui/Fulfilment | POST fulfilment
[**apis_ui_inspiration_cards_get**](DefaultApi.md#apis_ui_inspiration_cards_get) | **GET** /apis/ui/inspiration/cards | GET cards
[**apis_ui_login_loginwithcredential_post**](DefaultApi.md#apis_ui_login_loginwithcredential_post) | **POST** /apis/ui/login/loginwithcredential | POST loginwithcredential
[**apis_ui_pastshops_list_get**](DefaultApi.md#apis_ui_pastshops_list_get) | **GET** /apis/ui/pastshops/list | GET list
[**apis_ui_pies_categories_with_specials_get**](DefaultApi.md#apis_ui_pies_categories_with_specials_get) | **GET** /apis/ui/PiesCategoriesWithSpecials | GET piescategorieswithspecials
[**apis_ui_product_haveyouforgotten_get**](DefaultApi.md#apis_ui_product_haveyouforgotten_get) | **GET** /apis/ui/product/haveyouforgotten | GET haveyouforgotten
[**apis_ui_search_products_post**](DefaultApi.md#apis_ui_search_products_post) | **POST** /apis/ui/Search/products | POST products
[**apis_ui_search_suggestion_get**](DefaultApi.md#apis_ui_search_suggestion_get) | **GET** /apis/ui/Search/suggestion | GET suggestion
[**apis_ui_seo_metatags_post**](DefaultApi.md#apis_ui_seo_metatags_post) | **POST** /apis/ui/SeoMetatags | POST seometatags
[**apis_ui_settings_get**](DefaultApi.md#apis_ui_settings_get) | **GET** /apis/ui/settings | GET settings
[**apis_ui_shopper_authentication_method_get**](DefaultApi.md#apis_ui_shopper_authentication_method_get) | **GET** /apis/ui/shopper/AuthenticationMethod | GET authenticationmethod
[**apis_ui_trolley_get**](DefaultApi.md#apis_ui_trolley_get) | **GET** /apis/ui/Trolley | GET trolley
[**apis_ui_trolley_remove_post**](DefaultApi.md#apis_ui_trolley_remove_post) | **POST** /apis/ui/Trolley/Remove | POST remove
[**apis_ui_trolley_update_or_remove_items_post**](DefaultApi.md#apis_ui_trolley_update_or_remove_items_post) | **POST** /apis/ui/Trolley/UpdateOrRemoveItems | POST updateorremoveitems
[**apis_ui_user_preferences_has_done_checkout_onboarding_post**](DefaultApi.md#apis_ui_user_preferences_has_done_checkout_onboarding_post) | **POST** /apis/ui/UserPreferences/HasDoneCheckoutOnboarding | POST hasdonecheckoutonboarding
[**apis_ui_v2_search_count_get**](DefaultApi.md#apis_ui_v2_search_count_get) | **GET** /apis/ui/v2/Search/count | GET count

# **api_ui_v2_bootstrap_get**
> InlineResponse200 api_ui_v2_bootstrap_get()

GET bootstrap

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()

try:
    # GET bootstrap
    api_response = api_instance.api_ui_v2_bootstrap_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_ui_v2_bootstrap_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_ui_authentication_otp_post**
> InlineResponse2006 api_v3_ui_authentication_otp_post(body=body)

POST otp

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()
body = woolworths.AuthenticationOtpBody() # AuthenticationOtpBody |  (optional)

try:
    # POST otp
    api_response = api_instance.api_v3_ui_authentication_otp_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v3_ui_authentication_otp_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthenticationOtpBody**](AuthenticationOtpBody.md)|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_ui_checkout_digitalpay_instruments_get**
> InlineResponse20020 api_v3_ui_checkout_digitalpay_instruments_get(is_for_payment_agreement=is_for_payment_agreement)

GET instruments

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()
is_for_payment_agreement = 'is_for_payment_agreement_example' # str |  (optional)

try:
    # GET instruments
    api_response = api_instance.api_v3_ui_checkout_digitalpay_instruments_get(is_for_payment_agreement=is_for_payment_agreement)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v3_ui_checkout_digitalpay_instruments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_for_payment_agreement** | **str**|  | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_ui_fulfilment_feestructure_id_get**
> InlineResponse20024 api_v3_ui_fulfilment_feestructure_id_get(id)

GET feestructure by id

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()
id = 'id_example' # str | 

try:
    # GET feestructure by id
    api_response = api_instance.api_v3_ui_fulfilment_feestructure_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v3_ui_fulfilment_feestructure_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_ui_fulfilment_windows_get**
> InlineResponse20017 api_v3_ui_fulfilment_windows_get(area_id=area_id, fulfilment_method=fulfilment_method, address_id=address_id, suburb_id=suburb_id)

GET windows

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()
area_id = 1.2 # float |  (optional)
fulfilment_method = 'fulfilment_method_example' # str |  (optional)
address_id = 1.2 # float |  (optional)
suburb_id = 1.2 # float |  (optional)

try:
    # GET windows
    api_response = api_instance.api_v3_ui_fulfilment_windows_get(area_id=area_id, fulfilment_method=fulfilment_method, address_id=address_id, suburb_id=suburb_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v3_ui_fulfilment_windows_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area_id** | **float**|  | [optional] 
 **fulfilment_method** | **str**|  | [optional] 
 **address_id** | **float**|  | [optional] 
 **suburb_id** | **float**|  | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_ui_mylists_get**
> InlineResponse20013 api_v3_ui_mylists_get()

GET mylists

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()

try:
    # GET mylists
    api_response = api_instance.api_v3_ui_mylists_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v3_ui_mylists_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_ui_order_amending_get**
> InlineResponse2007 api_v3_ui_order_amending_get()

GET amending

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()

try:
    # GET amending
    api_response = api_instance.api_v3_ui_order_amending_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v3_ui_order_amending_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_ui_packaging_preferences_get**
> InlineResponse20025 api_v3_ui_packaging_preferences_get()

GET packagingpreferences

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()

try:
    # GET packagingpreferences
    api_response = api_instance.api_v3_ui_packaging_preferences_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v3_ui_packaging_preferences_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_ui_packaging_preferences_id_post**
> InlineResponse20025 api_v3_ui_packaging_preferences_id_post(id, body=body)

POST packagingpreferences by id

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()
id = 'id_example' # str | 
body = NULL # object |  (optional)

try:
    # POST packagingpreferences by id
    api_response = api_instance.api_v3_ui_packaging_preferences_id_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v3_ui_packaging_preferences_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_ui_trolley_update_post**
> InlineResponse20014 api_v3_ui_trolley_update_post(body=body)

POST trolley update

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()
body = woolworths.TrolleyUpdateBody() # TrolleyUpdateBody |  (optional)

try:
    # POST trolley update
    api_response = api_instance.api_v3_ui_trolley_update_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v3_ui_trolley_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrolleyUpdateBody**](TrolleyUpdateBody.md)|  | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_checkout_confirm_order_get**
> InlineResponse20029 apis_ui_checkout_confirm_order_get(order_id=order_id)

GET confirmorder

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()
order_id = 1.2 # float |  (optional)

try:
    # GET confirmorder
    api_response = api_instance.apis_ui_checkout_confirm_order_get(order_id=order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_checkout_confirm_order_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **float**|  | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_checkout_digital_pay_initialize_credit_card_iframe_post**
> InlineResponse20021 apis_ui_checkout_digital_pay_initialize_credit_card_iframe_post()

POST initializecreditcardiframe

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()

try:
    # POST initializecreditcardiframe
    api_response = api_instance.apis_ui_checkout_digital_pay_initialize_credit_card_iframe_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_checkout_digital_pay_initialize_credit_card_iframe_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_checkout_digital_pay_payment_post**
> InlineResponse20027 apis_ui_checkout_digital_pay_payment_post(body=body)

POST payment

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()
body = woolworths.DigitalPayPaymentBody() # DigitalPayPaymentBody |  (optional)

try:
    # POST payment
    api_response = api_instance.apis_ui_checkout_digital_pay_payment_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_checkout_digital_pay_payment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DigitalPayPaymentBody**](DigitalPayPaymentBody.md)|  | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_checkout_get**
> InlineResponse20016 apis_ui_checkout_get()

GET checkout

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()

try:
    # GET checkout
    api_response = api_instance.apis_ui_checkout_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_checkout_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_delivery_delivery_info_get**
> InlineResponse20023 apis_ui_delivery_delivery_info_get()

GET deliveryinfo

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()

try:
    # GET deliveryinfo
    api_response = api_instance.apis_ui_delivery_delivery_info_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_delivery_delivery_info_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_delivery_options_get**
> InlineResponse20018 apis_ui_delivery_options_get()

GET options

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()

try:
    # GET options
    api_response = api_instance.apis_ui_delivery_options_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_delivery_options_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_delivery_options_post**
> InlineResponse20019 apis_ui_delivery_options_post(body=body)

POST options

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()
body = woolworths.DeliveryOptionsBody() # DeliveryOptionsBody |  (optional)

try:
    # POST options
    api_response = api_instance.apis_ui_delivery_options_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_delivery_options_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeliveryOptionsBody**](DeliveryOptionsBody.md)|  | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_fulfilment_post**
> InlineResponse20022 apis_ui_fulfilment_post(body=body)

POST fulfilment

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()
body = woolworths.UiFulfilmentBody() # UiFulfilmentBody |  (optional)

try:
    # POST fulfilment
    api_response = api_instance.apis_ui_fulfilment_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_fulfilment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UiFulfilmentBody**](UiFulfilmentBody.md)|  | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_inspiration_cards_get**
> InlineResponse20012 apis_ui_inspiration_cards_get(url=url)

GET cards

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()
url = 'url_example' # str |  (optional)

try:
    # GET cards
    api_response = api_instance.apis_ui_inspiration_cards_get(url=url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_inspiration_cards_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**|  | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_login_loginwithcredential_post**
> InlineResponse2005 apis_ui_login_loginwithcredential_post(body=body)

POST loginwithcredential

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()
body = woolworths.LoginLoginwithcredentialBody() # LoginLoginwithcredentialBody |  (optional)

try:
    # POST loginwithcredential
    api_response = api_instance.apis_ui_login_loginwithcredential_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_login_loginwithcredential_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginLoginwithcredentialBody**](LoginLoginwithcredentialBody.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_pastshops_list_get**
> InlineResponse20028 apis_ui_pastshops_list_get()

GET list

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()

try:
    # GET list
    api_response = api_instance.apis_ui_pastshops_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_pastshops_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_pies_categories_with_specials_get**
> InlineResponse2002 apis_ui_pies_categories_with_specials_get()

GET piescategorieswithspecials

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()

try:
    # GET piescategorieswithspecials
    api_response = api_instance.apis_ui_pies_categories_with_specials_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_pies_categories_with_specials_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_product_haveyouforgotten_get**
> list[object] apis_ui_product_haveyouforgotten_get()

GET haveyouforgotten

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()

try:
    # GET haveyouforgotten
    api_response = api_instance.apis_ui_product_haveyouforgotten_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_product_haveyouforgotten_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_search_products_post**
> InlineResponse20011 apis_ui_search_products_post(body=body)

POST products

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()
body = woolworths.SearchProductsBody() # SearchProductsBody |  (optional)

try:
    # POST products
    api_response = api_instance.apis_ui_search_products_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_search_products_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchProductsBody**](SearchProductsBody.md)|  | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_search_suggestion_get**
> InlineResponse2009 apis_ui_search_suggestion_get(key=key)

GET suggestion

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()
key = 'key_example' # str |  (optional)

try:
    # GET suggestion
    api_response = api_instance.apis_ui_search_suggestion_get(key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_search_suggestion_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_seo_metatags_post**
> InlineResponse2003 apis_ui_seo_metatags_post(body=body)

POST seometatags

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()
body = woolworths.UiSeoMetatagsBody() # UiSeoMetatagsBody |  (optional)

try:
    # POST seometatags
    api_response = api_instance.apis_ui_seo_metatags_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_seo_metatags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UiSeoMetatagsBody**](UiSeoMetatagsBody.md)|  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_settings_get**
> list[InlineResponse2001] apis_ui_settings_get()

GET settings

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()

try:
    # GET settings
    api_response = api_instance.apis_ui_settings_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_settings_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_shopper_authentication_method_get**
> InlineResponse2004 apis_ui_shopper_authentication_method_get()

GET authenticationmethod

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()

try:
    # GET authenticationmethod
    api_response = api_instance.apis_ui_shopper_authentication_method_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_shopper_authentication_method_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_trolley_get**
> InlineResponse20015 apis_ui_trolley_get()

GET trolley

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()

try:
    # GET trolley
    api_response = api_instance.apis_ui_trolley_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_trolley_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_trolley_remove_post**
> InlineResponse2008 apis_ui_trolley_remove_post(body=body)

POST remove

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()
body = woolworths.TrolleyRemoveBody() # TrolleyRemoveBody |  (optional)

try:
    # POST remove
    api_response = api_instance.apis_ui_trolley_remove_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_trolley_remove_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrolleyRemoveBody**](TrolleyRemoveBody.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_trolley_update_or_remove_items_post**
> InlineResponse20026 apis_ui_trolley_update_or_remove_items_post(body=body)

POST updateorremoveitems

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()
body = woolworths.TrolleyUpdateOrRemoveItemsBody() # TrolleyUpdateOrRemoveItemsBody |  (optional)

try:
    # POST updateorremoveitems
    api_response = api_instance.apis_ui_trolley_update_or_remove_items_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_trolley_update_or_remove_items_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrolleyUpdateOrRemoveItemsBody**](TrolleyUpdateOrRemoveItemsBody.md)|  | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_user_preferences_has_done_checkout_onboarding_post**
> apis_ui_user_preferences_has_done_checkout_onboarding_post(body=body)

POST hasdonecheckoutonboarding

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()
body = woolworths.UserPreferencesHasDoneCheckoutOnboardingBody() # UserPreferencesHasDoneCheckoutOnboardingBody |  (optional)

try:
    # POST hasdonecheckoutonboarding
    api_instance.apis_ui_user_preferences_has_done_checkout_onboarding_post(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_user_preferences_has_done_checkout_onboarding_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserPreferencesHasDoneCheckoutOnboardingBody**](UserPreferencesHasDoneCheckoutOnboardingBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_ui_v2_search_count_get**
> InlineResponse20010 apis_ui_v2_search_count_get(search_term=search_term)

GET count

### Example
```python
from __future__ import print_function
import time
import woolworths
from woolworths.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = woolworths.DefaultApi()
search_term = 'search_term_example' # str |  (optional)

try:
    # GET count
    api_response = api_instance.apis_ui_v2_search_count_get(search_term=search_term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_ui_v2_search_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**|  | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

