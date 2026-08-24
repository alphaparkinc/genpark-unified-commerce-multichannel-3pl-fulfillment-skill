from client import UnifiedCommerceMultichannel3plFulfillmentClient

def main():
    client = UnifiedCommerceMultichannel3plFulfillmentClient()
    res = client.route_multichannel_fulfillment('Amazon_FBM', ['SKU_COAT_XL'], '10001')
    print('Order: ' + res['fulfillment_order_id'] + ' -> ' + res['assigned_3pl_warehouse'])
    print('Carrier: ' + res['delivery_carrier'] + ' ($' + str(res['shipping_rate_optimized_usd']) + ', ' + str(res['estimated_transit_days']) + ' days)')
    print('Inventory Synced: ' + ', '.join(res['inventory_synchronized_across_channels']))

if __name__ == '__main__':
    main()
