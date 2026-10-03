status=input("Enter order status: ")

match status:
    case "out_for_delivery":
        print("Your order is on the way")
    case "confirmed":
        print("Your order is confirmed")
    case "preparing":
        print("Your order is being prepared")
    case "placed":
        print("Your order has been placed")
    case "delivered":
        print("Your order has been delivered")
    case "cancelled":
        print("Your order has been cancelled")