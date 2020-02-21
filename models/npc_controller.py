class NPCController():
    def __init__(self):
        self._npc_keyring = {}

    def add_npc(self, name, npc_object):
        self._npc_keyring[name] = npc_object

    def get_npc(self, name):
        return self._npc_keyring[name]

    def get_all_npcs(self):
        return self._npc_keyring
