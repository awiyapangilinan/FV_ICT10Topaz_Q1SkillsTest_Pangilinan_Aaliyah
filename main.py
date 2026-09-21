from pyscript import document, display

def place_order(e):
    document.getElementById("output1").innerHTML = " " # clears previous result
    prod1 = document.getElementById("item1") 
    prod2 = document.getElementById("item2") 
    prod3 = document.getElementById("item3") 
    prod4 = document.getElementById("item4") 
    prod5 = document.getElementById("item5") 

    drinktotal = float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked + float(prod4.value) * prod4.checked + float(prod5.value) * prod5.checked

    size = document.querySelector("input[name='size']:checked")
    sprice = float(size.value)
    grandtotal = drinktotal + sprice

    addons = document.getElementById("addons")
    addons_price = float(addons.value)

    fixedprice = grandtotal + addons_price
    tax = fixedprice * 0.12 # VAT OF 12%
    tax_price = fixedprice + tax # order total + tax

    final_order = tax_price

    display(f"Subtotal: ₱{fixedprice}", target="output1")
    display(f"Tax: ₱{tax}", target="output1", append=True)
    display(f"Total: ₱{final_order}", target="output1", append=True)
    display("〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜", target="output1", append=True)
    display("Thankyou for choosing Madcha•̀ ᴖ •́", target="output1", append=True)