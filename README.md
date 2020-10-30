

# Juniper Networks Junos Collection
[![CI](https://zuul-ci.org/gated.svg)](https://dashboard.zuul.ansible.com/t/ansible/project/github.com/ansible-collections/junipernetworks.junos) <!--[![Codecov](https://img.shields.io/codecov/c/github/ansible-collections/vyos)](https://codecov.io/gh/ansible-collections/junipernetworks.junos)-->

The Ansible Juniper Networks Junos collection includes a variety of Ansible content to help automate the management of Juniper Networks Junos network appliances.

This collection has been tested against Juniper Networks Junos OS 18.4R1.

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.9.10,<2.11**.

Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.
<!--end requires_ansible-->

### Supported connections
The Juniper Networks Junos collection supports ``network_cli`` and ``netconf`` connections.

## Included content

<!--start collection content-->
### Cliconf plugins
Name | Description
--- | ---
[junipernetworks.junos.junos](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_cliconf.rst)|Use junos cliconf to run command on Juniper Junos OS platform

### Netconf plugins
Name | Description
--- | ---
[junipernetworks.junos.junos](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_netconf.rst)|Use junos netconf plugin to run netconf commands on Juniper JUNOS platform

### Modules
Name | Description
--- | ---
[junipernetworks.junos.junos_acl_interfaces](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_acl_interfaces_module.rst)|ACL interfaces resource module
[junipernetworks.junos.junos_acls](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_acls_module.rst)|ACLs resource module
[junipernetworks.junos.junos_banner](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_banner_module.rst)|Manage multiline banners on Juniper JUNOS devices
[junipernetworks.junos.junos_command](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_command_module.rst)|Run arbitrary commands on an Juniper JUNOS device
[junipernetworks.junos.junos_config](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_config_module.rst)|Manage configuration on devices running Juniper JUNOS
[junipernetworks.junos.junos_facts](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_facts_module.rst)|Collect facts from remote devices running Juniper Junos
[junipernetworks.junos.junos_interface](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_interface_module.rst)|(deprecated, removed after 2022-06-01) Manage Interface on Juniper JUNOS network devices
[junipernetworks.junos.junos_interfaces](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_interfaces_module.rst)|Junos Interfaces resource module
[junipernetworks.junos.junos_l2_interface](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_l2_interface_module.rst)|(deprecated, removed after 2022-06-01) Manage L2 Interface on Juniper JUNOS network devices
[junipernetworks.junos.junos_l2_interfaces](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_l2_interfaces_module.rst)|L2 interfaces resource module
[junipernetworks.junos.junos_l3_interface](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_l3_interface_module.rst)|(deprecated, removed after 2022-06-01) Manage L3 interfaces on Juniper JUNOS network devices
[junipernetworks.junos.junos_l3_interfaces](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_l3_interfaces_module.rst)|L3 interfaces resource module
[junipernetworks.junos.junos_lacp](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_lacp_module.rst)|Global Link Aggregation Control Protocol (LACP) Junos resource module
[junipernetworks.junos.junos_lacp_interfaces](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_lacp_interfaces_module.rst)|LACP interfaces resource module
[junipernetworks.junos.junos_lag_interfaces](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_lag_interfaces_module.rst)|Link Aggregation Juniper JUNOS resource module
[junipernetworks.junos.junos_linkagg](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_linkagg_module.rst)|(deprecated, removed after 2022-06-01) Manage link aggregation groups on Juniper JUNOS network devices
[junipernetworks.junos.junos_lldp](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_lldp_module.rst)|(deprecated, removed after 2022-06-01) Manage LLDP configuration on Juniper JUNOS network devices
[junipernetworks.junos.junos_lldp_global](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_lldp_global_module.rst)|LLDP resource module
[junipernetworks.junos.junos_lldp_interface](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_lldp_interface_module.rst)|(deprecated, removed after 2022-06-01) Manage LLDP interfaces configuration on Juniper JUNOS network devices
[junipernetworks.junos.junos_lldp_interfaces](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_lldp_interfaces_module.rst)|LLDP interfaces resource module
[junipernetworks.junos.junos_logging](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_logging_module.rst)|Manage logging on network devices
[junipernetworks.junos.junos_netconf](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_netconf_module.rst)|Configures the Junos Netconf system service
[junipernetworks.junos.junos_ospfv2](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_ospfv2_module.rst)|OSPFv2 resource module
[junipernetworks.junos.junos_ospfv3](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_ospfv3_module.rst)|OSPFv3 resource module
[junipernetworks.junos.junos_package](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_package_module.rst)|Installs packages on remote devices running Junos
[junipernetworks.junos.junos_ping](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_ping_module.rst)|Tests reachability using ping from devices running Juniper JUNOS
[junipernetworks.junos.junos_rpc](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_rpc_module.rst)|Runs an arbitrary RPC over NetConf on an Juniper JUNOS device
[junipernetworks.junos.junos_scp](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_scp_module.rst)|Transfer files from or to remote devices running Junos
[junipernetworks.junos.junos_static_route](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_static_route_module.rst)|(deprecated, removed after 2022-06-01) Manage static IP routes on Juniper JUNOS network devices
[junipernetworks.junos.junos_static_routes](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_static_routes_module.rst)|Static routes resource module
[junipernetworks.junos.junos_system](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_system_module.rst)|Manage the system attributes on Juniper JUNOS devices
[junipernetworks.junos.junos_user](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_user_module.rst)|Manage local user accounts on Juniper JUNOS devices
[junipernetworks.junos.junos_vlan](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_vlan_module.rst)|(deprecated, removed after 2022-06-01) Manage VLANs on Juniper JUNOS network devices
[junipernetworks.junos.junos_vlans](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_vlans_module.rst)|VLANs resource module
[junipernetworks.junos.junos_vrf](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_vrf_module.rst)|Manage the VRF definitions on Juniper JUNOS devices

<!--end collection content-->

Click the ``Content`` button to see the list of content included in this collection.

## Installing this collection

You can install the Juniper Networks Junos collection with the Ansible Galaxy CLI:

    ansible-galaxy collection install junipernetworks.junos

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: junipernetworks.junos
```
## Using this collection

You can call modules by their Fully Qualified Collection Namespace (FQCN), such as `junipernetworks.junos.junos_l2_interfaces`.
The following example task replaces configuration changes in the existing configuration on a Juniper Networks Junos network device, using the FQCN:

```yaml
---
  - name: "Replace provided configuration with device configuration"
    junipernetworks.junos.junos_l2_interfaces:
      config:
        - name: ge-0/0/3
          access:
            vlan: v101
        - name: ge-0/0/4
          trunk:
            allowed_vlans:
              - vlan30
            native_vlan: 50
      state: replaced
```

**NOTE**: For Ansible 2.9, you may not see deprecation warnings when you run your playbooks with this collection. Use this documentation to track when a module is deprecated.


### See Also:

* [Juniper Junos Platform options](https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).
* [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [Juniper Networks Junos collection repository](https://github.com/ansible-collections/junipernetworks.junos). See [Contributing to Ansible-maintained collections](https://docs.ansible.com/ansible/devel/community/contributing_maintained_collections.html#contributing-maintained-collections) for complete details.

You can also join us on:

- Freenode IRC - ``#ansible-network`` Freenode channel
- Slack - https://ansiblenetwork.slack.com

See the [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html) for details on contributing to Ansible.

### Code of Conduct
This collection follows the Ansible project's
[Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html).
Please read and familiarize yourself with this document.


## Release notes

Release notes are available [here](https://github.com/ansible-collections/junipernetworks.junos/blob/main/changelogs/CHANGELOG.rst).


## Roadmap

<!-- Optional. Include the roadmap for this collection, and the proposed release/versioning strategy so users can anticipate the upgrade/update cycle. -->

## More information

- [Ansible network resources](https://docs.ansible.com/ansible/latest/network/getting_started/network_resources.html)
- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
