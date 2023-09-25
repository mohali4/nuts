from .models import base_pattern as __base_pattern, pattern_decorate as __pattern

@__pattern
class engineName_pattern(__base_pattern):
    __allow_chars = 'a-z,A-Z,0-9'
    __minimum_chars = '5'
    __maximum_chars = '18'
    __pattern = f"[{__allow_chars}]{'{'+__minimum_chars+','+__maximum_chars+'}'}"
    pattern = f'{__pattern}'
    #               [a-z,A-Z,0-9]{5,18}

@__pattern
class enginePrefix_pattern(__base_pattern):
    __allow_chars = 'a-z,A-Z,0-9'
    __minimum_chars = '3'
    __maximum_chars = '10'
    __pattern = f"[{__allow_chars}]{'{'+__minimum_chars+','+__maximum_chars+'}'}"
    pattern = f'{__pattern}'
    #               [a-z,A-Z,0-9]{3,10}


@__pattern
class userID_pattern (__base_pattern):

    __minimum_user_id_chars = '5'
    __maximum_user_id_chars = '150'
    pattern = f"^{enginePrefix_pattern}://.{'{'+__minimum_user_id_chars+','+__maximum_user_id_chars+'}'}$" #type: ignore
    #              [a-z,A-Z,0-9]{3,10}//.{5,150}