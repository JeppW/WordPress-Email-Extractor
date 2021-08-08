# WordPress Email Extractor
A proof-of-concept tool for extracting a single user email address from a WordPress site. 

The script abuses the `search` parameter on the `/wp-json/wp/v2/users` WordPress REST API endpoint to extract a user email address character-by-character.

Note: This issue is public. Public ticket available at https://core.trac.wordpress.org/ticket/53784.
