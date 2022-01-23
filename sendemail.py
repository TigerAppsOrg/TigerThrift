#-----------------------------------------------------------------------
# sendemail.py
# Author: Katie Chou, Iroha Shirai, Katelyn Rodrigues
#-----------------------------------------------------------------------
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From

# send seller notification when a buyer has reserved their item 
# given seller and buyer info as dicts and item_name. 
# return true if successful or false if unsuccessful
def send_seller_reservation_notification(seller, buyer, item_name): 

    message = Mail(
        from_email= From('tigerthrift@princeton.edu', 'TigerThrift'),
        to_emails= seller['email']
    )

    message.dynamic_template_data = {
        'seller': seller['first_name'],
        'buyer': buyer['full_name'],
        'buyer_email': buyer['email'],
        'prodname': item_name,
        'buyer_phone': buyer['phone']
    }

    message.template_id = 'd-1c278b3e28f44bf999db67e7cad5b740'

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))
        return False

    return True

# send buyer notification when they have reserved an item 
# given seller and buyer info as dicts and item_name. 
# return true if successful or false if unsuccessful
def send_buyer_reservation_notification(seller, buyer, item_name): 

    message = Mail(
        from_email= From('tigerthrift@princeton.edu', 'TigerThrift'),
        to_emails= buyer['email']
    )

    message.dynamic_template_data = {
        'buyer': buyer['first_name'],
        'prodname': item_name,
        'seller_full_name': seller['full_name'],
        'seller_email': seller['email'],
        'seller_phone': seller['phone']
    }

    message.template_id = 'd-b4712667a3ad4eb1854be09dad326f58'

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))
        return False

    return True

# send buyer reminder when their item's reservation has <24hrs left to complete sale
# given seller and buyer info as dicts and item_name. 
# return true if successful or false if unsuccessful
def send_buyer_reservation_reminder(seller, buyer, item_name):
    message = Mail(
        from_email= From('tigerthrift@princeton.edu', 'TigerThrift'),
        to_emails= buyer['email']
    )

    message.dynamic_template_data = {
        'buyer': buyer['first_name'],
        'prodname': item_name,
        'seller': seller['full_name'],
        'Weblink': seller['email'],
        'seller_phone': seller['phone']
    }

    print("BUYER RESERVATION NOTIFICATION FOR ITEMNAME", item_name)
    print(str(message.dynamic_template_data))

    message.template_id = 'd-404ac834f3a9498e95fd649664f16db4'

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    
    except Exception as e:
        print(str(e))
        return False
    
    return True

# send seller reminder when one of their item's on reserve has <24hrs left to complete sale
# given seller and buyer info as dicts and item_name. 
# return true if successful or false if unsuccessful
def send_seller_reservation_reminder(seller, buyer, item_name):
    message = Mail(
        from_email= From('tigerthrift@princeton.edu', 'TigerThrift'),
        to_emails= seller['email']
    )

    message.dynamic_template_data = {
        'seller': seller['first_name'],
        'buyer': buyer['full_name'],
        'Weblink': buyer['email'],
        'prodname': item_name,
        'buyer_phone': buyer['phone']
    }

    print("SELLER RESERVATION NOTIFICATION FOR ITEMNAME", item_name)
    print(str(message.dynamic_template_data))

    message.template_id = 'd-eb5701ad9a20409a9ed516db6d799c72'

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    
    except Exception as e:
        print(str(e))
        return False
    
    return True

# send buyer notification when their item's reservation period has expired
# given seller and buyer info as dicts and item_name. 
# return true if successful or false if unsuccessful
def send_buyer_expiration_notification(seller, buyer, item_name):
    message = Mail(
        from_email= From('tigerthrift@princeton.edu', 'TigerThrift'),
        to_emails= buyer['email']
    )

    message.dynamic_template_data = {
        'buyer': buyer['first_name'],
        'prodname': item_name,
        'seller': seller['full_name'],
        'Weblink': seller['email'],
        'seller_phone': seller['phone']
    }

    print("BUYER EXPIRATION NOTIFICATION FOR ITEMNAME", item_name)
    print(str(message.dynamic_template_data))

    message.template_id = 'd-5f7b305252c54c1ba9ea7e0939a2a232'

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    
    except Exception as e:
        print(str(e))
        return False

    return True

# send seller notification when one of their items on reserve has a reservation period that has expired
# given seller and buyer info as dicts and item_name. 
# return true if successful or false if unsuccessful
def send_seller_expiration_notification(seller, buyer, item_name):
    message = Mail(
        from_email= From('tigerthrift@princeton.edu', 'TigerThrift'),
        to_emails= seller['email']
    )

    message.dynamic_template_data = {
        'seller': seller['first_name'],
        'buyer': buyer['full_name'],
        'Weblink': buyer['email'],
        'prodname': item_name,
        'buyer_phone': buyer['phone']
    }
    print("SELLER EXPIRATION NOTIFICATION FOR ITEMNAME", item_name)
    print(str(message.dynamic_template_data))

    message.template_id = 'd-a791cb3eded14e04bbdd2f9b8b972c7d'

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    
    except Exception as e:
        print(str(e))
        return False
    
    return True

# send seller notification if one of their selling items' reservations has been cancelled
# given seller and buyer info as dicts and item_name. 
# return true if successful or false if unsuccessful
def send_seller_cancellation(seller, buyer, item_name): 

    message = Mail(
        from_email= From('tigerthrift@princeton.edu', 'TigerThrift'),
        to_emails= seller['email']
    )

    message.dynamic_template_data = {
        'seller': seller['first_name'],
        'buyer': buyer['full_name'],
        'prodname': item_name
    }

    message.template_id = 'd-f24e67b37db54451bfec0ea408bd635e'

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    
    except Exception as e:
        print(str(e))
        return False

    return True

# send buyer notification when they have cancelled a reservation
# given seller and buyer info as dicts and item_name. 
# return true if successful or false if unsuccessful
def send_buyer_cancellation(seller, buyer, item_name): 

    message = Mail(
        from_email= From('tigerthrift@princeton.edu', 'TigerThrift'),
        to_emails= buyer['email']
    )

    message.dynamic_template_data = {
        'buyer': buyer['first_name'],
        'prodname': item_name
    }

    message.template_id = 'd-baec16aeca6145028ca16ebc6ef80e71'

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))
        return False

    return True


