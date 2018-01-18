import json 
import boto3

# show nice JSON and end script
def dump_and_exit(data):
        from bson import json_util
        print json.dumps(data, indent=4, sort_keys=True, default=json_util.default)
        exit(0)  

def main():
    
    PROFILES = (#'team_1',
        #'team)_2'
    )
    
    for profile in PROFILES:
        print "working on {}...".format(profile)
    
        session = boto3.Session(profile_name=profile)
        data = session.client('ec2').describe_instances()
        data = session.client('ec2').describe_vpcs()
        data = session.client('ec2').describe_security_groups()
        data = session.client('ec2').describe_network_acls()
        
        #dump_and_exit(data)
        
        # get list of all VPCs in current profile
        vpcs = []
        for reservation in data['Reservations']:
            for instance in reservation['Instances']:
                vpcs.append(instance.get('VpcId'))  
        
        # remove duplicates
        vpcs = list(set(vpcs))
        
        # ACLs in VPCs
        acls = session.client('ec2').describe_network_acls()
        
        #print acls
        
        # search for instances assigned to specific VPC
        for vpc in vpcs: 
            print "{}: ".format(vpc)
            
            if vpc is None:
                print "{} have no instances".format(vpc)
                #continue
            
            # display ACLs for current VPC
            entries = []
            for acl in acls['NetworkAcls']:
                if vpc == acl.get('VpcId'):
                    for entrie in acl['Entries']:
                        ports = entrie.get('PortRange', "")
                        action = entrie.get('RuleAction', "")
                        if len(ports):
                            ports = "from port {} to {}".format(ports['From'], ports['To'])
                            
                        entries.append("CIDR: {} RuleNumber: {} {} Action: {}".format(entrie['CidrBlock'], entrie['RuleNumber'], ports, action))
            
            entries = list(set(entries)) 
            
            print "ACLs:"
            for entrie in entries:
                print " " * 4, entrie                        
                    
            print "Instances:"
            for reservation in data['Reservations']:
                for instance in reservation['Instances']:
                    if vpc == instance.get('VpcId'):
                        print " " * 4,
                        print instance.get('PrivateIpAddress'),
                        print instance.get('State')['Name'],
                        print "security group:", instance.get('SecurityGroups')[0]['GroupId']
  
        
    return


if __name__ == "__main__":
    main()