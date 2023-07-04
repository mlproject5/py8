import streamlit as st
import random
import string
import re


st.set_page_config(page_title='Magic Card', page_icon='mc.png', layout="centered", initial_sidebar_state="auto", menu_items=None)

def gpg():
    def generate_google_play_code():
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) + ' ' + \
               ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) + ' ' + \
               ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) + ' ' + \
               ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        return code

    def is_valid_google_play_code(code):
        code_parts = code.split(' ')
        if len(code_parts) != 4:
            return False
        if not all(len(part) == 4 for part in code_parts):
            return False
        if not all(part.isalnum() for part in code_parts):
            return False
        return True

    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Google Play Gift "
        "Card</h1></center>",
        unsafe_allow_html=True)

    st.markdown(
        "<style>.stButton>button {margin: 0 auto; display: block;}</style>",
        unsafe_allow_html=True
    )

    if st.button("Generate Google Play Code"):
        google_play_code = generate_google_play_code()
        st.code(google_play_code)
        if is_valid_google_play_code(google_play_code):
            st.success("Valid Google Play Gift Card !!")
        else:
            st.error("Invalid Google Play Gift Card !!")



def nf():
    def generate_netflix_code():
        netflix_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        return netflix_code

    def is_valid_netflix_code(netflix_code):
        if len(netflix_code) != 12:
            return False
        if not all(char.isalnum() for char in netflix_code):
            return False
        return True

    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Netflix Gift Card</h1></center>",
        unsafe_allow_html=True)

    st.markdown(
        "<style>.stButton>button {margin: 0 auto; display: block;}</style>",
        unsafe_allow_html=True
    )

    if st.button("Generate Netflix Code"):
        netflix_code = generate_netflix_code()
        st.code(netflix_code)
        if is_valid_netflix_code(netflix_code):
            st.success("Valid Netflix Gift Card !!")
        else:
            st.error("Invalid Netflix Gift Card !!")


def ag():
    def generate_amazon_code():
        amazon_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) + '-' + \
                      ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) + '-' + \
                      ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        return amazon_code

    def is_valid_amazon_code(amazon_code):
        code_parts = amazon_code.split('-')
        if len(code_parts) != 3:
            return False
        if len(code_parts[0]) != 4 or len(code_parts[1]) != 6 or len(code_parts[2]) != 4:
            return False
        if not all(part.isalnum() for part in code_parts):
            return False
        return True

    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Amazon Gift Card</h1></center>",
        unsafe_allow_html=True)

    st.markdown(
        "<style>.stButton>button {margin: 0 auto; display: block;}</style>",
        unsafe_allow_html=True
    )

    if st.button("Generate Amazon Code"):
        amazon_code = generate_amazon_code()
        st.code(amazon_code)
        if is_valid_amazon_code(amazon_code):
            st.success("Valid Amazon Gift Card !!")
        else:
            st.error("Invalid Amazon Gift Card !!")



def itg():
    def generate_itunes_code():
        code_length = 16
        chars = string.ascii_uppercase + string.digits
        itunes_code = random.choice(string.ascii_uppercase) + ''.join(random.choices(chars, k=code_length - 1))
        return itunes_code

    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>iTunes Gift Card</h1></center>",
        unsafe_allow_html=True)

    st.markdown(
        "<style>.stButton>button {margin: 0 auto; display: block;}</style>",
        unsafe_allow_html=True
    )

    if st.button("Generate iTunes Code"):
        itunes_code = generate_itunes_code()
        st.code(itunes_code)
        st.success("Valid iTunes Gift Card !!")




def eg():
    def generate_ebay_number():
        ebay_number = ''.join(random.choices(string.digits, k=13))
        return ebay_number

    def format_ebay_number(ebay_number):
        formatted_number = ' '.join([ebay_number[:3], ebay_number[3:6], ebay_number[6:9], ebay_number[9:]])
        return formatted_number

    def is_valid_ebay_number(ebay_number):
        if len(ebay_number) != 13:
            return False
        if not ebay_number.isdigit():
            return False
        return True

    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>eBay Gift Card</h1></center>",
        unsafe_allow_html=True)

    st.markdown(
        "<style>.stButton>button {margin: 0 auto; display: block;}</style>",
        unsafe_allow_html=True
    )

    if st.button("Generate eBay Number"):
        ebay_number = generate_ebay_number()
        formatted_number = format_ebay_number(ebay_number)
        st.code(formatted_number)
        if is_valid_ebay_number(ebay_number):
            st.success("Valid eBay Gift Card !!")
        else:
            st.error("Invalid eBay Gift Card !!")


def ppg():
    def generate_paypal_number():
        paypal_number = ''.join(random.choices(string.digits, k=16))
        return paypal_number

    def format_paypal_number(paypal_number):
        formatted_number = ' '.join([paypal_number[i:i + 4] for i in range(0, len(paypal_number), 4)])
        return formatted_number

    def is_valid_paypal_number(paypal_number):
        if len(paypal_number) != 16:
            return False
        if not all(char.isdigit() for char in paypal_number):
            return False
        return True

    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>PayPal Gift Card</h1></center>",
        unsafe_allow_html=True)

    st.markdown(
        "<style>.stButton>button {margin: 0 auto; display: block;}</style>",
        unsafe_allow_html=True
    )

    if st.button("Generate PayPal Number"):
        paypal_number = generate_paypal_number()
        formatted_number = format_paypal_number(paypal_number)
        st.code(formatted_number)
        if is_valid_paypal_number(paypal_number):
            st.success("Valid PayPal Gift Card !!")
        else:
            st.error("Invalid PayPal Gift Card !!")


def swg():
    def generate_steam_number():
        steam_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' + \
                       ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' + \
                       ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        return steam_number

    def is_valid_steam_number(steam_number):
        steam_parts = steam_number.split('-')
        if len(steam_parts) != 3:
            return False
        for part in steam_parts:
            if len(part) != 5:
                return False
            if not all(char.isalnum() for char in part):
                return False
        return True

    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Steam Gift "
        "Card</h1></center>",
        unsafe_allow_html=True)

    st.markdown(
        "<style>.stButton>button {margin: 0 auto; display: block;}</style>",
        unsafe_allow_html=True
    )

    if st.button("Generate Steam Number"):
        steam_number = generate_steam_number()
        st.code(steam_number)
        if is_valid_steam_number(steam_number):
            st.success("Valid Steam Gift Card !!")
        else:
            st.error("Invalid Steam Gift Card !!")


def xbg():
    def generate_xbox_number():
        xbox_number = '-'.join([''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for _ in range(5)])
        return xbox_number

    def is_valid_xbox_number(xbox_number):
        xbox_parts = xbox_number.split('-')
        if len(xbox_parts) != 5:
            return False
        for part in xbox_parts:
            if len(part) != 5:
                return False
            if not all(char.isalnum() for char in part):
                return False
        return True

    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Xbox Gift "
        "Card</h1></center>",
        unsafe_allow_html=True)

    st.markdown(
        "<style>.stButton>button {margin: 0 auto; display: block;}</style>",
        unsafe_allow_html=True
    )

    if st.button("Generate Xbox Number"):
        xbox_number = generate_xbox_number()
        st.code(xbox_number)
        if is_valid_xbox_number(xbox_number):
            st.success("Valid Xbox Gift Card !!")
        else:
            st.error("Invalid Xbox Gift Card !!")


def hma():
    def generate_hma_license_key():
        key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) + '-' + \
              ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) + '-' + \
              ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return key

    def is_valid_hma_license_key(key):
        key_parts = key.split('-')
        if len(key_parts) != 3:
            return False
        if not all(len(part) == 6 for part in key_parts):
            return False
        if not all(part.isalnum() for part in key_parts):
            return False
        return True

    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>HMA VPN License "
        "Key</h1></center>",
        unsafe_allow_html=True)

    st.markdown(
        "<style>.stButton>button {margin: 0 auto; display: block;}</style>",
        unsafe_allow_html=True
    )

    if st.button("Generate HMA License Key"):
        hma_license_key = generate_hma_license_key()
        st.code(hma_license_key)
        if is_valid_hma_license_key(hma_license_key):
            st.success("Valid License Key !!")
        else:
            st.error("Invalid License Key !!")


def express():
    def generate_code():
        code = 'E' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=22))
        return code

    def is_valid_code(code):
        if len(code) != 23:
            return False
        if code[0] != 'E':
            return False
        if not all(char.isalnum() for char in code):
            return False
        return True

    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>ExpressVPN Activation "
        "Code</h1></center>",
        unsafe_allow_html=True)

    st.markdown(
        "<style>.stButton>button {margin: 0 auto; display: block;}</style>",
        unsafe_allow_html=True
    )

    if st.button("Generate Code"):
        code = generate_code()
        st.code(code)
        if is_valid_code(code):
            st.success("Valid Activation Code !!")
        else:
            st.error("Invalid Activation Code !!")


def sk():
    def generate_key():
        prefix = "sk_live_"
        key = prefix + ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=24))
        return key

    def is_valid_key(key):
        prefix = "sk_live_"
        if len(key) == 24:
            return False
        if not key.startswith(prefix):
            return False
        if not all(char.isalnum() for char in key[len(prefix):]):
            return False
        return True

    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>SK Live Key</h1></center>",
        unsafe_allow_html=True)

    st.markdown(
        "<style>.stButton>button {margin: 0 auto; display: block;}</style>",
        unsafe_allow_html=True
    )

    if st.button("Generate Key"):
        key = generate_key()
        st.code(key)
        if is_valid_key(key):
            st.success("Valid SK Key !!")
        else:
            st.error("Invalid SK Key !!")



def main():
    st.sidebar.markdown("<h1 style='font-family: Comic Sans MS; font-weight: 600; font-size: 32px;'>Magic "
                "Card</h1></center>", unsafe_allow_html=True)
    selected_sidebar = st.sidebar.radio("Please Select One", ["Google Play", "Netflix","Amazon","iTunes","eBay","Paypal","Steam","Xbox","HMA VPN","Express VPN","SK Key"])

    if selected_sidebar == "Google Play":
        gpg()
    elif selected_sidebar == "Netflix":
        nf()
    elif selected_sidebar == "Amazon":
        ag()
    elif selected_sidebar == "iTunes":
        itg()
    elif selected_sidebar == "eBay":
        eg()
    elif selected_sidebar == "Paypal":
        ppg()
    elif selected_sidebar == "Steam":
        swg()
    elif selected_sidebar == "Xbox":
        xbg()
    elif selected_sidebar == "HMA VPN":
        hma()
    elif selected_sidebar == "Express VPN":
        express()
    elif selected_sidebar == "SK Key":
        sk()

    st.sidebar.markdown("<h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 12px;'>Multiple GiftCard "
                        "Generator and Checker "
                        "Coming Soon...</h1></center>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
