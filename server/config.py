'''
Set environment-based configs here. 
'''
class ProductionConfig(object):
    pass

class DevelopmentConfig(ProductionConfig):
    pass

class TestingConfig(ProductionConfig):
    pass

def get_config(debug=False, testing=False):
    if testing:
        print("Testing mode...")
        return TestingConfig
    elif debug:
        print("Development mode...")
        return DevelopmentConfig
    else:
        print("Production mode.")
        return ProductionConfig