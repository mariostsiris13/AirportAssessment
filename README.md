# AirportAssessment
markdown
Copy code
# Προσομοίωση Ουράς Προτεραιότητας στο Αεροδρόμιο

Αυτός ο κώδικας σε Python υλοποιεί μια βασική προσομοίωση ουράς προτεραιότητας για τη διαχείριση αιτημάτων προσγείωσης και απογείωσης αεροπλάνων σε ένα αεροδρόμιο. Επιτρέπει την προτεραιοποίηση ορισμένων αεροπλάνων έναντι άλλων και περιλαμβάνει βασική διαχείριση σφαλμάτων για να αποτρέψει το κούρσεμα κατά την προσπάθεια αποστολής απόκρισης από μια κενή ουρά.

## Χαρακτηριστικά

- **Χειρισμός Προτεραιότητας**: Επιτρέπει την προτεραιοποίηση επείγοντων αιτημάτων όπως επείγουσες προσγειώσεις ή επείγουσες απογειώσεις.
- **Διαχείριση Σφαλμάτων**: Βασική διαχείριση σφαλμάτων αποτρέπει το κούρσεμα κατά την προσπάθεια αποστολής απόκρισης από μια κενή ουρά.
- **Απλή Υλοποίηση**: Ο κώδικας είναι απλός και εύκολος στην κατανόηση, κατάλληλος για αρχάριους και γρήγορες τροποποιήσεις.

## Χρήση

1. Κλώνος ή κατέβασμα του αποθετηρίου.
2. Εκτέλεση του αρχείου `airport.py` χρησιμοποιώντας την Python.
3. Ακολούθησε τις οδηγίες για να προσομοιώσεις αιτήματα προσγείωσης και απογείωσης αεροπλάνων.

```bash
python airport.py
Περιορισμοί
Απόδοση: Οι λειτουργίες enqueue και dequeue έχουν γραμμική πολυπλοκότητα χρόνου στη χειρότερη περίπτωση, που είναι κατάλληλη για μεγάλες ουρές.
Εγκλεισμός: Η εσωτερική κατάσταση της ουράς είναι ανοιχτή
Χειρισμός Σφαλμάτων: Περιορισμένη διαχείριση σφαλμάτων για σενάρια πέρα ​​από τα κενά καταχωρήσεων, όπως μη έγκυρες εισόδους ή υπέρβαση χωρητικότητας ουράς.
Ευελιξία: Έλλειψη υποστήριξης για δυναμική αλλαγή μεγέθους της ουράς και επιπλέον χαρακτηριστικά όπως η δυνατότητα προβολής του επάνω μέρους της ουράς χωρίς αποστολή.
