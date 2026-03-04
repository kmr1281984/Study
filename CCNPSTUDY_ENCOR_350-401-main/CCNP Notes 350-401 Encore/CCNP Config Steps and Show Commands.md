



show vtp status ::: view vtp status
show int trunk ::: Show command to View Trunks
show int fa0/0 switchport ::: show command to view interface switchport configs

Configure Layer 3 Portchannel > no switchport > ip address "IP" "Subnet" > int ran fa0/0  1 > no switchport > channelgroup "#" mode "lacp or pagp"

show etherchannel summary ::: view etherchannel summary

Configure RSTP :: spanningtree mode rapidpvst (on all devices) > Configure portfast on non switch interfaces > int gi0/0 > spanningtree portfast

show spanningtree "#"
show spanningtree vlan "#" ::: view spanning tree for RSTP
show spanningtree vlan "#" root primary ::: view root information

Configure MST ::: spanningtree mst configuration > name "NAME" > revision "# that I control" > instances "#" vlan "range ex 100200" > spanningtree mst "##" root primary > spanningtree mst "#" root secondary > spanningtree mode mst

show spanningtree vlan "#" ::: view spanning tree for MST

Configure OSPF (Traditional)::: router ospf "#" > network "IP" "WC" area "#" > int gi 0/0 > network pointtopoint (Optional)
Configure OSPF (New Style) ::: router ospf "#" > int fa0/0 > ip ospf "#" area "#" 
Configure OSPF (summarize ospf route) ::: router ospf "#" > area "#" range "IP" "Sub" 
Configure OSPF (authentication) ::: int fa0/0 > ip ospf authentication messagedigest > ip ospf messagedigestkey "#" md5 "KEYWORD"

show ip ospf neighbor
show ip ospf interface
show ip ospf database

Configure BGP ::: router bgp "#" > neighbor "IP" remoteas "#" >neighbor "IP" updatesource "lo0" > neighbor "IP" ebgpmultihop "# of hops from device"

show ip bgp summary
show ip route

Configure NTP on Server ::: ntp master stratum "# value (1) from atomic clock" >  
Configure NTP on Client ::: ntp server "IP of Server" 

show ntp associations 
show ntp status

Configure PAT ::: ip accesslist standard "Name or #" > permit "IP" "WC" > ip nat source list "ACL" "interface or pool" "overload" > int gi0/0 > ip nat inside > int gi0/1 > ip nat outside

show ip nat translations



Configure NetFlow (flow record) ::: flow record "NAME" > match "" > collect interface "out or in" > collect counter bytes > collect counter packets >

Configure NetFlow (flow exporter) ::: flow exporter "NAME" > destinations "IP" > source "INT or IP" > transport "tcp or udp" "Port" > exportprotocol "NETFLOW VERSION"

Configure NetFlow (flow monitor) ::: flow monitor "NAME" > record "NAME of FLOW RECORD" > exporter "NAME OF EXPORTER" > exit > int "PHYSICAL OR VLAN" > ip flow monitor "NAME of FLOW MONITOR" "input or output"

Configure IP SLA ::: ip sla "#" > icmp-echo "IP" source-ip "IP" > frequency "# " > ip sla schedule "Entry Number" life "seconds" > ip sla schedule "Entry Number" start-time now


Configure CoPP 
1. access-list "#" ... > 
2. class-map "name" > match access-group "ACL #" >
3. policy-map "Name" > class "CLASS-MAP NAME" > police rate "units" pps > conform action "ACTION" >exit
4. config t > control-plane > service-policy "in or out" "NAME"