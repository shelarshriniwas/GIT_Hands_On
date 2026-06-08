# program_10_Cloud_storage_simulation.py

class AWSCloud:

    def storage(self):

        print("AWS S3 Storage")


class AzureCloud:

    def storage(self):

        print("Azure Blob Storage")


a = AWSCloud()
z = AzureCloud()

a.storage()
z.storage()