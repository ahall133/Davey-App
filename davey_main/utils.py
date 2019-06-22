def product_calculator(product, carrier):
    application = 'You will need to mix {} for your {} of carrier.'

    if product == 'agpro':
        rate = carrier/100
        rate = str(rate)
        carrier = str(carrier)
        mix = application.format(rate+" bags",carrier +" gallons")
        return mix

    if product == 'polyphos':
        rate = carrier/50
        rate= str(rate)
        carrier = str(carrier)
        mix = application.format(rate+ " gallons",carrier+" gallons")
        return mix

    if product == 'adams':
        ratio = carrier/100
        r_rate = ratio*64
        r_rate = str(r_rate)
        carrier = str(carrier)
        mix = application.format(r_rate+ ' ounces',carrier+" gallons" )
        return mix
    
    if product == 'cambistat':
        ratio = carrier/11
        r_rate = ratio*1
        r_rate = str(r_rate)
        carrier = str(carrier)
        mix = application.format(r_rate+' gallons',carrier+" gallons")
        return mix

    if product == 'florel':
        ratio = carrier/10
        r_rate = ratio/4
        r_rate = str(r_rate)
        carrier = str(carrier)
        mix = application.format(r_rate+' gallons',carrier+" gallons")
        return mix
        

def product_id(product):
    if product == 'agpro':
        real_product = 'Davey Arborgreen Pro (30-10-7)'
        return real_product

    if product == 'polyphos':
        real_product = 'Polyphosphite 30 (0-0-27)'
        return real_product

    if product == 'adams':
        real_product = 'Adams Earth Biostimulant'
        return real_product

    if product == 'cambistat':
        real_product = 'Cambistat Tree Growth Regulator'
        return real_product

    if product == 'florel':
        real_produt = 'Florel Growth Regulator'
        return real_produt

def rate(product, carrier):
    if product == 'agpro':
        product_amount = "15lbs per 100 gallons"
        return product_amount

    if product == 'polyphos':
        product_amount = "2 gallons per 100 gallons"
        return product_amount

    if product == 'adams':
        product_amount = "64 ounces per 100 gallons"
        return product_amount

    if product == 'cambistat':
        product_amount = "1 gallon per 11 gallons"
        return product_amount

    if product == 'florel':
        product_amount = '1 quart per 10 gallons (2.5 gallons per 100 gallons)'
        return product_amount


        
        
        
    

        


