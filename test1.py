import json 
import boto3
from tabulate import tabulate

def main():
    
    PROFILES = (#'team_1',
        #'team)_2'
    )
    
    results = []
    id = 0
    
    ALLOWED_PORTS = [80, 443]

    for profile in PROFILES:
        
        # we are now looking only on production env
        if "_stage" in profile:
            continue
        
        print "working on ".format(profile)
    
        session = boto3.Session(profile_name=profile)
        sgs = session.client('ec2').describe_instance_status()

        for sg in sgs['InstanceStatuses']:

            affected_instances = 0
            response = session.client('ec2').describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']},])
            for reservation in response['Reservations']:
                affected_instances += len(reservation.get('Instances', ''))
            
            reason = []
        results.append([id, profile])
    
    print tabulate(results, headers=['ID', 'Profile'])
    
    
    for item in results:
        for entry in item:
            print "{};".format(entry),
        print
    
    return

if __name__ == "__main__":
    main()