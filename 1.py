import libtorrent as lt

ses = lt.session()
ses.listen_on(6881, 6891)
downloads = []
