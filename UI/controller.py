import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCerca(self, e):
        source = self._model.getObjectFromId(int(self._view._txtIdOggetto.value))

        lun = self._view._ddLun.value
        if lun is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Attenzione, selezionare un parametro Lunghezza.", color="red"))
            self._view.update_page()
            return
        lunInt = int(lun)
        path, pesoTot = self._model.getOptPath(source, lunInt)

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(
            f"Cammino che parte da {source} trovato con peso totale {pesoTot}."))
        for p in path:
            self._view.txt_result.controls.append(ft.Text(p))
        self._view.update_page()

    def handleAnalizzaOggetti(self, e):
        self._model.build_graph()
        dettagli = self._model.getGraphDetails()
        self._view.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"nodi: {dettagli[0]}, archi: {dettagli[1]}", color="red"))
        self._view.update_page()

    def handleCompConnessa(self,e):
        idoggetto = self._view._txtIdOggetto.value
        connessaNum = self._model.getConnessa(idoggetto)
        self._view.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"nodi connessi a {idoggetto}: {connessaNum}", color="red"))
        self._view.update_page()


