def product_calculator(product, carrier):
    application = 'Using {} gallons you will need to mix {} of {} at a mix rate of {} per {}.'
    if product == 'agpro':
        product_amount = 25
        rate = carrier//product_amount
        rate = str(rate)
        print(rate)
        mix = application.format(carrier, rate+" bags","Arborgreen Pro","50lbs","100 gallons of carrier")
        return mix
        

        


