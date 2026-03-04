#flashcards/ccnp/encor/Architecture 


#flashcards/ccnp/encor/Architecture/HA_and_FT

Stateful Switchover (SSO) ::: redundant brain in devices
NonStop Forwarding (NSF) ::: need to use for FHRP to work with SSO

#flashcards/ccnp/encor/Architecture/WLAN

CAPWAP ::: uses Datagram Transport Layer Sec (DTLS)
CAPWAP Control Channel :: UDP port 5246
CAPWAP Data Channel :: UDP Port 5247
WLC ::: provides bridging, forwarding and encryption
CAPWAP :: Control and Provisioning of Wireless Access Points
FlexConnect Remote Branch ::: if WLC is lost Lightweight AP (LAP) still functions 
RFID ::: 4 channels on 2.4 ghz used for tracking
CCX radio 
RSSI Measurement 

#flashcards/ccnp/encor/Architecture/SDWan

SDWAN Option ::: Meraki 
Vmanage ::: Network Managing system (single pane of glass)
vSmart controller ::: DTLS tunnels to SDWAN routers; establish Overlay management Protocol (OMP) neighborships
vedge router ::: cisco ios xe
vbond orchestrator ::: auth between vsmart and vedge devices
vbond orchestrator ::: only sdwan device requiring a public ip address
v analytics 

#flashcards/ccnp/encor/Architecture/SDAccess

underlay ::: uses ISIS if automated 
Overlay ::: uses VXLAN LISP Cisco Trust SEC
LISP ::: SDAccess uses it as the Control Plane 
VXLAN ::: SDAccess uses it as the Data Plane
Cisco TrustSec ::: SDAccess uses it as the Policy Plane
Controller Layer SDAccess ::: these operate at what layer on the SDaccess model Cisco DNA Center and Cisco ISE
Management Layer SDAccess ::: Cisco DNA center operates at this later of the SD access model 
Fabric Components ::: virtual network, host pool, scalable group tags, anycast gateway

#flashcards/ccnp/encor/Architecture/QOS_Concepts

Best Effort (BE) ::: QOS approach where more bandwidth is added to deal with issues (Default)
IntServ ::: QOS approach RSVP Protocol signal ahead for reservation
DiffServ ::: QOS classified traffic, close to edge, has a trust boundary (where class and marking is done)
NBAR2 ::: QOS DiffServ classification method
cos bits ::: diffserv Layer 2 QOS marking
MPLS EXP bits diffserv Layer 2.5 QOS marking
DSCP and IP Precedence (IPP) ::: diffserv Layer 3 QOS marking
TOS ::: 8 bits that contain DSCP (6bits) expedited congestion notification (ECN) (2 bits)
Policing ::: Drop or Remark
Single rate two color ::: Policer that does Drop or remark 
Single rate three color ::: Policer that does Drop remark or permit 
tworate three color maker ::: Policer that does Bursting and absolute don't go above this value Drop remark or permit
DiffServe Congestion management ::: combines Class based weighted fair queuing (CBWFQ) (three queues) and low latency queuing (LLQ) (One Queue)
RED vs WRED random early detection
DiffServ Link Conditioning ::: compressing traffic Link Frag and Interleaving (LFI)

#flashcards/ccnp/encor/Architecture/HW_and_SW_Switch_Mech

CEF ::: MAC is not in adj table not arp cache for CEF
CEF ::: takes information from Routing Info Base (RIB) and adds it to the Forward Info Base (FIB)
Terniery Content Addressable Memory Table (TCAM) ::: replaced the MAC Table

#flashcards/ccnp/encor/Virtuallization/VRF

Create VRF :: in conf t use "ip vrf NAME"
<!SR:!20260218,3,250>
Use Ping with VRF :: "ping vrf NAME IP"
<!SR:!20260219,4,270>
add VRF to INT :: ip vrf forwarding NAME
<!SR:!20260218,3,250>
Set up OSPF with VRF :: router ospf "#" vrf NAME then network commands
<!SR:!20260216,1,230>

#flashcards/ccnp/encor/Virtuallization/GRE

GRE ::: sends encapsulated multicast traffic as unicast 

#flashcards/ccnp/encor/Virtuallization/IPSEC

IPSEC ::: Optional for IPV4 Mandatory for IPV6
IPSEC Phase 1 ::: create isakmp policy
IPSEC transformset ::: dictates how the data will be encrypted and authenticated
IPSEC profile

#flashcards/ccnp/encor/Virtuallization/LISP

LISP :: Location IS/Seperation Protocol
LISP ::: Works alot like DNS
LISP Tunneling Router (xTR) ::: registers host in LISP mapping database
Endpoint Identifier (EID) ::: LISP assigned IP Address
Virtual Network Interface (NVI) :::
RLOC ::: xTR IP
LISP site ::: all LISP rtrs and EIDs
Ingress Tunnel Router ::: LISP encapsulates packets destined for outside LISP site
Egress Tunnel Router ::: deencapsulates packets before sending to LISP site
xTR ::: any router that performs ITR or ETR functions 
PITR ::: handles traffic from nonlisp sites destined for eids
PETR ::: handles traffic from EIDs destined for non LISP sites
PxTR ::: Proxy Tunnel Routers  PITRs and PETRs
RLOC ::: IP address of an ETR that is internet facing or network core facing 
Map Server (MS) ::: EID to RLOC Database
Map Resolver (MR ) ::: answers queries

#flashcards/ccnp/encor/Virtuallization/VXLAN

VXLAN ::: overlays L2 Net with L3 network acting as underlay
VXLAN ::: AKA macinudp encapsulation
Equal cost multipathing (ECMP) ::: 
VXLAN Network ID (VNID) ::: 24 bit segment ID that defines broadcast domain
Virtual Tunnel Endpoint (VTEP) ::: device that performs encap and deencap
Network Virtual Interface (NVI) ::: the logical interface where encap and deencap occurs
VXLAN ::: uses security group tags (SGTs)

#flashcards/ccnp/encor/Infrastructure/Trunks_Dot1Q

#flashcards/ccnp/encor/Infrastructure/VTP

#flashcards/ccnp/encor/Infrastructure/Etherchannel

lacp ::: Active Passive etherchannel
pagp ::: Desirable auto etherchannel
switchport mode trunk then switchport nonegotiate ::: Create static links on interfraces
Steps to create a layer 3 Port Channel :: Create Portchannel > then no switchport > ip address "IP" "Subnet" > int ran fa0/0  1 > no switchport > channelgroup "#" mode "lacp or pagp"

#flashcards/ccnp/encor/Infrastructure/RSTP 

802.1d ::: classic spanning tree protocol
802.1w ::: rapid spanning tree
Config RSTP :: spanningtree mode rapidpvst (on all devices) > Configure portfast on non switch interfaces > int gi0/0 > spanningtree portfast
RSTP ::  backbonefast uplinkfast automatically included in ?
portfast ::: configure on interfaces not connected to a switch

#flashcards/ccnp/encor/Infrastructure/MST

802.1s ::: Multiple spanning tree protocol (MST)
Config MST ::: spanningtree mst configuration > name "NAME" > revision "# that I control" > instances "#" vlan "range ex 100200" > spanningtree mst "##" root primary > spanningtree mst "#" root secondary > spanningtree mode mst

#flashcards/ccnp/encor/Infrastructure/Routing_Protocols/EIGRP

EIGRP ::: Hybrid, DUAL Algorithm, Unequal cost load balancing, Bandwidth and delay

#flashcards/ccnp/encor/Infrastructure/Routing_Protocols/OSPF

OSPF ::: LinkState, SPF algorithm, equal cost load balancing, cost
Configure OSPF (Traditional)::: router ospf "#" > network "IP" "WC" area "#" > int gi 0/0 > network pointtopoint (Optional)
Configure OSPF (New Style) ::: router ospf "#" > int fa0/0 > ip ospf "#" area "#" 
network pointtopoint ::: OSPF command that removes DR/BDR elections (only two routers exist)
stub ::: Routing command that filters out redistributed prefixes
Configure OSPF (summarize ospf route) ::: router ospf "#" > area "#" range "IP" "Sub" 
Configure OSPF (authentication) ::: int fa0/0 > ip ospf authentication messagedigest > ip ospf messagedigestkey "#" md5 "KEYWORD"

#flashcards/ccnp/encor/Infrastructure/Routing_Protocols/eBGP 

Configure BGP ::: router bgp "#" > neighbor "IP" remoteas "#" >neighbor "IP" updatesource "lo0" > neighbor "IP" ebgpmultihop "# of hops from device"

#flashcards/ccnp/encor/Infrastructure/Layer1_Wireless

Effective Isotropic Radiated Power (EIRP) ::: Strength of signal with Wireless Antenna
Free space path loss ::: Attenuation of Signal as it moves through the air
Received Signal Strength Indicator (RSSI) ::: Rating of signal strength 
Signal to Noise Ratio (SNR) ::: Noise floor munis Signal Strength 
802.11n ::: 2.4 and 5 GHz, spatial multiplexing, Multiple Input and Multiple Output (MIMO)
802.11ac ::: 5 Ghz
802.11ax ::: 2.4 and 5 Ghz 
Cisco Client Extensions (CCX) ::: versions 1 through 5, endorsement from Cisco that features like security, performance, fast roaming, and power management are supported

#flashcards/ccnp/encor/Infrastructure/Access_Points/AP_Modes_Ant_Types

AP Modes ::: Local, Monitor, flexconnect
Local ::: AP that is default, idle time assists with other services
Monitor :: AP that can perform IDS, and based services
FlexConnect ::: AP can switch to VLAN operation
Flex + bridge ::: AP can do flexconnect and can be used in a mesh
Cisco Spectrum Expert (SEconnect) ::: AP Software for monitoring and site analysis
Omnidirectional ::: Dipole and integrated antennas
Yagi and Dish ::: Directional antennas

#flashcards/ccnp/encor/Infrastructure/Access_Points/AP_Discovery_and_Joins

Autonomous AP ::: Vlans and Trunks AP
Lightweight AP ::: CAPWAP AP
Steps AP Boot and WLC Discovery ::: Ip Address and IOS Image > WLC Discovery (internal); DHCP/DNS; Broadcast DHCP Option 43 Default DNS for WLC (CISCOCAPWAPCONTROLLER.localdomain) > CAPWAP  DTLS (Digital Certificates) > WLC Join >Download image > Download Config > Run State > Reset (If we choose)
Primed ::: WLC 1st Choice
Discover ::: WLC 2nd Choice
Least Loaded ::: WLC 3rd Choice

#flashcards/ccnp/encor/Infrastructure/Layer2_and_Layer3_Roaming 

Autonomous Roaming ::: Simple Roaming
Lightweight ::: WLC handles the process, Intracontroller and Intercontroller
Intracontroller ::: Roaming from one domain defined on the WLC to another domain on the same WLC
Intercontroller ::: Roaming from one WLC to another Anchor (source) Foreign (New WLC joined as we roam)
802.11r ::: Protocol assists with roaming
Cisco Centralized Key Management (CCKM) ::: assists with roaming and found in Cisco Client Extensions (CCX) 
Key caching ::: technology assists with roaming
Mobility Groups ::: Assist with Layer 3 Intercontroller Roams

#flashcards/ccnp/encor/Infrastructure/WLC_Troubleshooting

Troubleshoot Wireless Lan Steps ::: 1. Client in range > 2. Ap Associated > 3. Client Receives IP
WLC AP Status Codes ::: Start > Association > Authentications > DHCP > Online

#flashcards/ccnp/encor/Infrastructure/NTP 

Configure NTP on Server ::: ntp master stratum "# value (1) from atomic clock"
<!SR:!20260218,3,250!20260218,3,250>
Configure NTP on Client ::: ntp server "IP of Server" 

#flashcards/ccnp/encor/Infrastructure/NAT_PAT

Configure PAT ::: ip accesslist standard "Name or #" > permit "IP" "WC" > ip nat source list "ACL" "interface or pool" "overload" > int gi0/0 > ip nat inside > int gi0/1 > ip nat outside
Inside Local ::: Client Private IP
Inside Global ::: Client Public IP
Outside local ::: Server Private IP
Outside Global ::: Server Public IP

#flashcards/ccnp/encor/Infrastructure/FHRP 

HSRP ::: (Classic) Cisco Proprietary  Uses Virtual Router Active and Standby
VRRP ::: Open standard Version of HSRP, Master and Backup, Can use physical ip address
GLBP ::: Cisco Proprietary Can load balance, uses Active Virtual Gateway (AVG) and Active Virtual Forwarder (AVF) 
Active Virtual Gateway (AVG) ::: gives out virtual mac address to Active Virtual Forwarder (AVF)

#flashcards/ccnp/encor/Infrastructure/Multicast

Multicast Protocols ::: Uses Reverse Path Forwarding Check(RFPC)
Reverse Path Forwarding Check(RFPC) ::: When a multicast traffic arrives on router > Router checks unicast routing table to see if traffic is arriving on expected interface. If not the router drops it
Protocol Independent Multicast (PIM) ::: Doesn't matter the routing type (Ex. Static, EIGRP OSPF Etc..)
Dense Mode (DM) ::: Floods (multicast everywhere), Prunes or Grafts (where no multicast receiver received) Shows up in source distribution tree (in Routing Table ("S, G")
Sparse Mode (SM) ::: uses a  Multicast sent to Rendezvous Point (RP) > RP builds shared distribution tree >RP shares shared distribution tree with other multicast servers  (in Routing Table ("Star, G")
Internet Group Management Protocol (IGMP) ::: Clients signal they want to receive multicast traffic V2 or V3
Internet Group Management Protocol (IGMP) Snooping ::: Switchs Eavesdrop in IGMP traffic to intelligently forward Multicast Traffic

#flashcards/ccnp/encor/NetworkAssurance/CLI_Tools

debug ip routing ::: shows ip routing deb info
debug ip packet "accesslist #"
ping wizard ::: just "ping"

#flashcards/ccnp/encor/NetworkAssurance/Syslog

syslog ::: system messaging 

Console Logging ::: 
Monitor Logging ::: 
Buffer Logging ::: 

Configure Syslog ::: logging "console buffered monitor" "Number 07" > logging host "ip to send logs" (Optional)

#flashcards/ccnp/encor/NetworkAssurance/NetFlow_and_Flexible_Netflow

Flow Records ::: Defines what to capture
Flow Monitor ::: Applied to the interface
Flow Exporter ::: Tool to send the traffic to a remote system
Flow Sampler ::: limits to load on the router gathering data

Configure NetFlow (flow record) ::: flow record "NAME" > match "" > collect interface "out or in" > collect counter bytes > collect counter packets >

Configure NetFlow (flow exporter) ::: flow exporter "NAME" > destinations "IP" > source "INT or IP" > transport "tcp or udp" "Port" > export-protocol "NETFLOW VERSION"

Configure NetFlow (flow monitor) ::: flow monitor "NAME" > record "NAME of FLOW RECORD" > exporter "NAME OF EXPORTER" > exit > int "PHYSICAL OR VLAN" > ip flow monitor "NAME of FLOW MONITOR" "input or output"

#flashcards/ccnp/encor/NetworkAssurance/SPAN_RSPAN_ERSPAN

Configure span ::: monitor session "#" source interface gi 0/2 > monitor session "#" destination interface g 0/3

Configure rspan ::: vlan "#" > remote span > monitor session "#" source interface gi0/1 tx > monitor session "#" destination remote vlan "#" > monitor session "#" source remote vlan "#" > monitor session "#" destination interface gi0/2

SPAN ::: on one switch 
RSPAN ::: From one swtich to another
ERSPAN ::: Perform SPAN in a routed environment

#flashcards/ccnp/encor/NetworkAssurance/IP_SLA

Configure IP SLA ::: ip sla "#" > icmp-echo "IP" source-ip "IP" > frequency "# " > ip sla schedule "Entry Number" life "seconds" > ip sla schedule "Entry Number" start-time now
Distant end needs to run the IP SLA Responder
show ip sla "#" statistics 

#flashcards/ccnp/encor/NetworkAssurance/DNA_Center_Workflow



#flashcards/ccnp/encor/NetworkAssurance/NETCONF_RESTCONF

NETCONF ::: just xml
RESTCONF ::: Can do XML or JSON
YANG ::: Data models used by RestConf and NetConf

#flashcards/ccnp/encor/Security/Access_Control_List


Configure ACLS ::: 


#flashcards/ccnp/encor/Security/Control_Plan_Policing_CoPP


Control Plan Policing (CoPP)

Configure CoPP 
1. access-list "#" ... > 
2. class-map "name" > match access-group "ACL #" >
3. policy-map "Name" > class "CLASS-MAP NAME" > police rate "units" pps > conform action "ACTION" >exit
4. config t > control-plane > service-policy "in or out" "NAME"

#flashcards/ccnp/encor/Security/REST_API_Security

Applications > "Northbound API" > Controller > "Southbound API" > Data Plane
Restful APIs ::: use CRUD

#flashcards/ccnp/encor/Security/Wireless_Security_Features

WebAuth
PSK
Extensible Authentication Protocol (EAP) ::: use with 802.1x


WLC can support Local-EAP 

#flashcards/ccnp/encor/Security/Network_Security_Design

ASA w/Firepower ::: newer ASA has Firepower Module

Firepower Threat Defense (FTD) ::: Can do firewalling and IP in one chassis

Embedded Advanced Malware Prevention (AMP) ::: Endpoint security for devices

Firepower Management Console (FMC) ::: Physical device 

Cisco TALOS ::: 


#flashcards/ccnp/encor/Automation/JSON

JSON ::: Curly Braces "Key:Value Pair" 


#flashcards/ccnp/encor/Automation/YANG

YANG ::: overall model used for netconf and restconf
YANG ::: 
Data Model ::: dictates structure, syntax, and semantics

#flashcards/ccnp/encor/Automation/Rest_API_Response_Codes

1xx ::: Informational
2xx ::: Success
3xx ::: Redirection
4xx ::: Client Error
5xx ::: Server Error


#flashcards/ccnp/encor/Automation/EEM

Embedded Event Manager (EEM) ::: everything local to the device 

EEM Server ::: Applets, Scripts, EEM Policy Director, Event Detector, 

Configure EEM ::: event manager applet "NAME" > event syslog pattern "string" occurs "#" > action "Number 1.0 then 1.1 etc" syslog msg "String"

#flashcards/ccnp/encor/Automation/Orchestration_Tools






















