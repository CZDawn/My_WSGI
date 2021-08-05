from views import Index, About, Contacts

# set of bindings: path - controller
routes = {
    '/': Index(),
    '/about/': About(),
    '/contacts/': Contacts(),
}
