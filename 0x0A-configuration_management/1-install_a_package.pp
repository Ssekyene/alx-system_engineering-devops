# Install flask v: 2.1.0 from pip3, werkzeug must be v: 2.1.1 or < 3.*

package { 'flask':
ensure   => '2.1.0',
provider => 'pip3'
}
