"""
This code sample shows Prebuilt Receipt operations with the Azure Form Recognizer client library. 
The async versions of the samples require Python 3.6 or later.

To learn more, please visit the documentation - Quickstart: Document Intelligence (formerly Form Recognizer) SDKs
https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?pivots=programming-language-python
"""

from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see 
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""
endpoint = "https://eastus.api.cognitive.microsoft.com/"
key = "bfd52fa437c94798bda8d91518f24b74"

# sample document
file_path = "real-food.jpg"

document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

with open(file_path, mode = 'rb') as form_data:
    poller = document_analysis_client.begin_analyze_document("prebuilt-receipt", form_data)
    receipts = poller.result()

    for idx, receipt in enumerate(receipts.documents):
        print("--------Recognizing receipt #{}--------".format(idx + 1))
        receipt_type = receipt.doc_type
        if receipt_type:
            print(
                "Receipt Type: {}".format(receipt_type)
            )
        merchant_name = receipt.fields.get("MerchantName")
        if merchant_name:
            print(
                "Merchant Name: {} has confidence: {}".format(
                    merchant_name.value, merchant_name.confidence
                )
            )
        transaction_date = receipt.fields.get("TransactionDate")
        if transaction_date:
            print(
                "Transaction Date: {} has confidence: {}".format(
                    transaction_date.value, transaction_date.confidence
                )
            )
        if receipt.fields.get("Items"):
            print("Receipt items:")
            for idx, item in enumerate(receipt.fields.get("Items").value):
                print("...Item #{}".format(idx + 1))
                item_description = item.value.get("Description")
                if item_description:
                    print(
                        "......Item Description: {} has confidence: {}".format(
                            item_description.value, item_description.confidence
                        )
                    )
                item_quantity = item.value.get("Quantity")
                if item_quantity:
                    print(
                        "......Item Quantity: {} has confidence: {}".format(
                            item_quantity.value, item_quantity.confidence
                        )
                    )
                item_price = item.value.get("Price")
                if item_price:
                    print(
                        "......Individual Item Price: {} has confidence: {}".format(
                            item_price.value, item_price.confidence
                        )
                    )
                item_total_price = item.value.get("TotalPrice")
                if item_total_price:
                    print(
                        "......Total Item Price: {} has confidence: {}".format(
                            item_total_price.value, item_total_price.confidence
                        )
                    )
        subtotal = receipt.fields.get("Subtotal")
        if subtotal:
            print(
                "Subtotal: {} has confidence: {}".format(
                    subtotal.value, subtotal.confidence
                )
            )
        tax = receipt.fields.get("TotalTax")
        if tax:
            print("Tax: {} has confidence: {}".format(tax.value, tax.confidence))
        tip = receipt.fields.get("Tip")
        if tip:
            print("Tip: {} has confidence: {}".format(tip.value, tip.confidence))
        total = receipt.fields.get("Total")
        if total:
            print("Total: {} has confidence: {}".format(total.value, total.confidence))
        print("--------------------------------------")
