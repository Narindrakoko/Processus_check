import psutil

def get_process_list():
  """
  Récupère et affiche la liste des processus en cours d'exécution.
  """

  # Récupère tous les processus en cours d'exécution
  processes = psutil.process_iter()

  # Affiche les informations sur chaque processus
  for process in processes:
    try:
      # Obtient le nom du processus
      process_name = process.name()

      # Obtient l'ID du processus (PID)
      pid = process.pid

      # Obtient le nom d'utilisateur du propriétaire du processus
      username = process.username()

      # Obtient l'état du processus (ex: 'en cours d'exécution', 'en veille')
      process_status = process.status()

      # Obtient l'utilisation du CPU par le processus
      cpu_percent = process.cpu_percent()

      # Obtient la mémoire utilisée par le processus
      memory_usage = process.memory_info().rss / 1024 **2  # En Mo

      # Affiche les informations formatées
      print(f"  - Nom: {process_name} (PID: {pid}, Utilisateur: {username})")
      print(f"    État: {process_status}")
      print(f"    Utilisation CPU: {cpu_percent:.2f}%")
      print(f"    Mémoire utilisée: {memory_usage:.2f} Mo")
      print("-" * 50)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
      pass  # Ignore les exceptions si le processus n'existe plus ou si l'accès est refusé

if __name__ == "__main__":
  get_process_list()
