# Install nginx with Puppet

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Ensure the Nginx service is running and enabled at boot
service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/sites-available/default'],
}

# Ensure the default site configuration file is present and properly configured
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;
	index index.html index.htm;

	server_name _;

	location / {
      	try_files $uri $uri/ =404;
	}

	location /redirect_me {
      	return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}

	error_page 404 /404.html;
	location = /404.html {
		root /var/www/html;
      	internal;
	}
}
 "
  notify => Service['nginx'],

}

# Create the custom 404.html page
file { '/var/www/html/404.html':
  ensure => 'present',
  content => "Ceci n'est pas une page\n",
  require => Package['nginx'],
}

# Ensure the site is enabled by creating a symlink in sites-enabled
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  notify  => Service['nginx'],
}

# Ensure the document root directory exists
file { '/var/www/html':
  ensure => directory,
}

# Ensure the index.html file is present with the required content
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  notify  => Service['nginx'],
}
