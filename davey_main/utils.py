def product_calculator(product, carrier):
    application = 'You will need to mix {} for your {} of carrier.'

    if product == 'agpro':
        rate = carrier/100
        rate = str(rate)
        mix = application.format(rate+" bags","100 gallons")
        print(rate)
        return mix
        
def product_id(product):
    if product == 'agpro':
        real_product = 'Davey Arborgreen Pro 30-10-7'
        return real_product

def rate(product, carrier):
    if product == 'agpro':
        product_amount = "15lbs per 100 gallons"
        return product_amount


        
        
        
    

        


