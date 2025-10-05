from pyscript import  document 

m7 = { "m1": 300,"m2": 190,"m3": 160, "m4": 560, "m5": 400, "m6": 260 }
menu1 = {"m1": "Onion Soup", "m2": "Croissants","m3": "Cremebrulee", "m4": "Beef Bourguignon with Barley Miso", "m5":"Duck Confit With Caraway", "m6":"Grilled Ratatouille with Herb Dressing", }

def profile(e):
        l1 = document.getElementById("name").value 
        l2 = document.getElementById("address").value
        l3 = document.getElementById("phone").value

        selected_items = []
        total= 0 
        for item_id in m7:
            checkbox = document.getElementById(item_id)
            if checkbox.checked: 
                selected_items.append(menu1[item_id])
                total += m7[item_id]

        items_str = ", ".join(selected_items) if selected_items else "None"

    
        message = f"""
        <span style="font-size:20px; font-weight:bold; color: #f2ecb1; font-family:Verdana, sans-serif;">Good Day! Here is your order information:</span> <br><br><br>
        <span style="font-size:15px; font-weight:bold; color: #f2ecb1; font-family:Verdana, sans-serif;">Customer name: {l1} </span>
        <br><br>
        <span style="font-size:15px; font-weight:bold; color: #f2ecb1; font-family:Verdana, sans-serif;">Customer Address: {l2} </span>
        <br> <br>
        <span style="font-size:15px; font-weight:bold; color: #f2ecb1; font-family:Verdana, sans-serif;">Customer Phone Number: {l3} </span>
        <br><br>
        <span style="font-size:15px; font-weight:bold; color: #f2ecb1; font-family:Verdana, sans-serif;">Food/s Ordered: {items_str} </span>
        <br> <br>
        <span style="font-size:15px; font-weight:bold; color: #f2ecb1; font-family:Verdana, sans-serif;"> Total of order: ₱ {total} </span>
        """
        document.getElementById("order").innerHTML = message
