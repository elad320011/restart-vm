from pyVim.connect import SmartConnectNoSSL
import vmutils
untouchables = ["vm name and addresses not able to touch"]


def reboot(vm_name):
    if vm_name not in untouchables:
        c = SmartConnectNoSSL(host="x.x.x.x", user="administrator@vsphere.local", pwd=<password>)
        searchindex = c.RetrieveContent().searchIndex
        searchip= searchindex.FindAllByIp(ip=vm_name,vmSearch=True)
        if len(searchip) != 0:
            searchip[0].RebootGuest()
            return True
        else:
            try:
                vm = vmutils.get_vm_by_name(c, vm_name)
                vm.RebootGuest()
                return True
            except:
                return False
