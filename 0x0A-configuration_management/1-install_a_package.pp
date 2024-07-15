# Install flask v: 2.1.0 from pip3
# ensure that werkzeug version is less than 3.* for
# compatibility, for my case werkzeug v: 2.1.1
# you can use `pip3 show` to check for versions

package { 'flask':
ensure   => '2.1.0',
provider => 'pip3'
}
