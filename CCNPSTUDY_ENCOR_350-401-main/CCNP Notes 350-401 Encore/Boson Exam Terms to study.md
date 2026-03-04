

#flaschards/CCNP/ENCOR/Architecture
-vBond :: Manages the Orchestration Plane
-VSmart ::  Manages the Control plane
-vEdge router :: Manages the data plane
<!--SR:!2026-02-16,1,228-->
-vManage NMS :: Manages the management
<!--SR:!2026-02-16,1,228-->
-Traffic Shaping :: Buffers excess traffic and uses leaky bucket to smooth traffic
-VRRP :: FHRP master backup
-Locations/ID separation Protocol LISP ::: basis for Cisco SD-Access fabric control access
-VXLAN ::: basis for the sd access data plane
<!--SR:!2026-02-17,2,240!2000-01-01,1,250-->
-CIsco TrustSec ::: basis of the Sd-Access Policy Plane
-Intermediate System to Intermediate System IS-IS :: routing protocol can be the basis of the underlay network
<!--SR:!2026-02-16,1,220-->
-SSO — _Stateful Switchover_ ::: high-availability feature that allows a standby supervisor (or route processor) to take over immediately if the active one fails — **without interrupting network traffic**.
<!--SR:!2000-01-01,1,250!2026-02-16,1,220-->
-Nonstop Forwarding (NSF) ::: A routing capability that allows a device to continue forwarding traffic during a control-plane failure or switchover, preventing routing reconvergence.
<!--SR:!2000-01-01,1,250!2026-02-16,1,228-->
-Route Processor Redundancy (RPR) :: A redundancy mode in which a standby route processor exists but is not fully synchronized and must reload and restart routing protocols after a failure.
-edge node : provides connectivity to fabric access points in cisco SD access
-Cisco Presence Analytics Service ::: enables the use of wireless tech to study customer behavior
<!--SR:!2000-01-01,1,250!2026-02-16,1,210-->


#flaschards/CCNP/ENCOR/Infrastructure

-isis password ::: interface authentication used to auth hello messages
-DHCPv6 Client Request steps :: Solicit Advertise Request  Reply

#flaschards/CCNP/ENCOR/Automation

-Sync yes ::: eem checks the value of the exit status




#flaschards/CCNP/ENCOR/NetworkAssurance


#flaschards/CCNP/ENCOR/Security

-WPA2 ::: uses AES-CCMP

#flaschards/CCNP/ENCOR/Virtuallization

-1 ::: Hub to spoke is DMVPN Phase __
<!--SR:!2000-01-01,1,250!2026-02-17,2,238-->
-2 :: spoke to spoke is DMVPN Phase __
<!--SR:!2026-02-16,1,218-->
-3 ::: spoke to spoke with NHRP is DMVPN Phase __
<!--SR:!2000-01-01,1,250!2026-02-18,3,258-->



