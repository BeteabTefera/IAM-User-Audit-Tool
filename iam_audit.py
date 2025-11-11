import boto3
from datetime import datetime,timezone

def main():
    iam = boto3.client('iam')
    users = iam.list_users()['Users']
    
    print(f"{'User':20} {'Last Used':25} {'Active Keys'}")
    print("-" * 60)
    
    for user in users:
        username = user['UserName']
        
        # Get password last used
        pwd_last_used = user.get('PasswordLastUsed')
        if pwd_last_used:
            pwd_last_used = pwd_last_used.strftime("%Y-%m-%d")
        else:
            pwd_last_used = "Never logged in"
        
        # List access keys
        keys = iam.list_access_keys(UserName=username)['AccessKeyMetadata']
        active_keys = [k for k in keys if k['Status'] == 'Active']
        
        print(f"{username:20} {pwd_last_used:25} {len(active_keys)} active keys")
    
    print("\n✅ Audit complete. Use this to enforce IAM best practices!")

if __name__ == "__main__":
    main()
