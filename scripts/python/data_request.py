import cdsapi

# dataset 
dataset = "reanalysis-era5-single-levels"

# definições da request dos dados:
# dados de precipitação, registrados às 00h, de 2005 a 2020 e da região da América do Sul
request = {
        'product_type': 'reanalysis',
        'variable': 'total_precipitation',
        'year': [
            '2005','2006','2007','2008','2009',
            '2010','2011','2012','2013','2014',
            '2015','2016','2017','2018','2019','2020'
        ],
        'month': [
            '01','02','03','04','05','06',
            '07','08','09','10','11','12'
        ],
        'day': [
            '01','02','03','04','05','06','07','08','09','10',
            '11','12','13','14','15','16','17','18','19','20',
            '21','22','23','24','25','26','27','28','29','30','31'
        ],
        'time': '00:00',
        'area': [5, -75, -30, -35],
        'format': 'netcdf',
    }

# request
c = cdsapi.Client()
c.retrieve(dataset, request, '../../data/raw/precip_2005_2020.nc')
