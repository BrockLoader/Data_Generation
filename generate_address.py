
def generate_address(amt):

    import pandas as pd
    import secrets as sc

    allstreetdata = pd.read_csv('brisbanestreets.csv')

    streetnames = allstreetdata[['STREET NAME']].copy()
    streetnames = streetnames.drop_duplicates()
    streetnames = streetnames.reset_index()
    streetnames = streetnames.drop(['index'], axis=1)

    streetTypes = allstreetdata[['STREET TYPE']].copy()
    streetTypes = streetTypes.drop_duplicates()
    streetTypes = streetTypes.reset_index()
    streetTypes = streetTypes.drop(['index'], axis=1)

    suburbs = allstreetdata[['SUBURB']].copy()
    suburbs = suburbs.drop_duplicates()
    suburbs = suburbs.reset_index()
    suburbs = suburbs.drop(['index'], axis=1)

    loop_count = 0
    address_list = list()

    while loop_count < int(amt):
        # generate street number
        StreetNumber = sc.SystemRandom().randint(1, 98)
        # generate street name
        StreetName = str(streetnames.iloc[sc.SystemRandom().randint(0, len(streetnames) - 1)].values[0]).title()
        # generate street type
        StreetType = str(streetTypes.iloc[sc.SystemRandom().randint(0, len(streetTypes) - 1)].values[0]).title()
        # generate suburb
        Suburb = str(suburbs.iloc[sc.SystemRandom().randint(0, len(streetTypes) - 1)].values[0]).title()
        # generate postcode
        PostCode = sc.SystemRandom().randint(4000,4999)
        # set state
        State = "QLD"

        #str(StreetNumber), StreetName, StreetType + ',', Suburb + ',', str(PostCode) + ',', State
        FullAddress = str(StreetNumber) + ' -  ' + StreetName + ' ' + StreetType + ' -' + ' ' + Suburb + ' -' + ' ' + str(PostCode) + ' - ' + State
        
        #if FullAddress in address_list:
            #break

        address_list.append(FullAddress)

        loop_count = loop_count + 1

    return address_list
