import importlib
if 64 - 64: i11iIiiIii
def OO0o ( name1 , name2 ) :
 Oo0Ooo = importlib . util . spec_from_file_location ( name1 , name2 )
 O0O0OO0O0O0 = importlib . util . module_from_spec ( Oo0Ooo )
 Oo0Ooo . loader . exec_module ( O0O0OO0O0O0 )
 return O0O0OO0O0O0
 # actual grading
def iiiii ( inp_f ) :
 print ( 'On Time Submission - 10pts' )
 ooo0OO = inp_f [ : - 3 ]
 if 18 - 18: II111iiii . OOO0O / II1Ii / oo * OoO0O00
 if 2 - 2: ooOO00oOo % oOo0O0Ooo * Ooo00oOo00o . oOoO0oo0OOOo + iiiiIi11i
 try :
  print ( '\n\n\nEmpty Test (20 pts):' )
  O0O0OO0O0O0 = OO0o ( ooo0OO , inp_f )
  Ii1I = O0O0OO0O0O0 . LinkedList ( )
  print ( '\nFirst link None - 5pts' )
  try :
   print ( '\nExpected Output: None' + '    ' + 'Output : ' + str ( Ii1I . first ) )
  except :
   print ( '\nTest failed to run' )
  print ( '\nget_num_links - 5pts' )
  try :
   print ( '\nExpected Output: 0' + '    ' + 'Output : ' + str ( Ii1I . get_num_links ( ) ) )
  except :
   print ( '\nTest failed to run' )
  print ( '\nis_empty - 5pts' )
  try :
   print ( '\nExpected Output: True' + '    ' + 'Output : ' + str ( Ii1I . is_empty ( ) ) )
  except :
   print ( '\nTest failed to run' )
  print ( '\nis_sorted - 5pts' )
  try :
   print ( '\nExpected Output: True' + '    ' + 'Output : ' + str ( Ii1I . is_sorted ( ) ) )
  except :
   print ( '\nTest failed to run' )
 except :
  print ( '\nEmpty Test Failed' )
  if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
  if 97 - 97: oO0o0ooO0 - IIII / O0oO - o0oO0
  if 100 - 100: oo
 try :
  print ( '\n\n\nInsertion / Reverse / Search Test (40 pts):' )
  O0O0OO0O0O0 = OO0o ( ooo0OO , inp_f )
  I1Ii11I1Ii1i = O0O0OO0O0O0 . LinkedList ( )
  print ( '\ninsert_first / insert_last - 5pts' )
  print ( '\nInserting 3,2,1 with insert_first. Inserting 5,6,7 with insert_last.' )
  for Ooo in [ 3 , 2 , 1 ] :
   I1Ii11I1Ii1i . insert_first ( Ooo )
  for o0oOoO00o in [ 5 , 6 , 7 ] :
   I1Ii11I1Ii1i . insert_last ( o0oOoO00o )
  i1 = [ ]
  oOOoo00O0O = I1Ii11I1Ii1i . first
  while oOOoo00O0O != None :
   i1 . append ( oOOoo00O0O . data )
   oOOoo00O0O = oOOoo00O0O . next
  try :
   print ( '\nExpected Contents: [1,2,3,5,6,7]' + '    ' + 'Contents : ' + str ( i1 ) )
  except :
   print ( '\nTest failed to run' )
  print ( '\nis_sorted - 5pts' )
  try :
   print ( '\nExpected Output: True' + '    ' + 'Output : ' + str ( I1Ii11I1Ii1i . is_sorted ( ) ) )
  except :
   print ( '\nTest failed to run' )
  print ( '\nget_num_links - 5pts' )
  try :
   print ( '\nExpected Output: 6' + '    ' + 'Output : ' + str ( I1Ii11I1Ii1i . get_num_links ( ) ) )
  except :
   print ( '\nTest failed to run' )
  print ( '\nis_empty - 5pts' )
  try :
   print ( '\nExpected Output: False' + '    ' + 'Output : ' + str ( I1Ii11I1Ii1i . is_empty ( ) ) )
  except :
   print ( '\nTest failed to run' )
  print ( '\ninsert_in_order - 5pts' )
  print ( '\nInserting 4 in order' )
  I1Ii11I1Ii1i . insert_in_order ( 4 )
  i1 = [ ]
  oOOoo00O0O = I1Ii11I1Ii1i . first
  while oOOoo00O0O != None :
   i1 . append ( oOOoo00O0O . data )
   oOOoo00O0O = oOOoo00O0O . next
  try :
   print ( '\nExpected Contents: [1,2,3,4,5,6,7]' + '    ' + 'Contents : ' + str ( i1 ) )
  except :
   print ( '\nTest failed to run' )
  print ( '\nfind_ordered - 5pts' )
  print ( '\nSearching for 0' )
  try :
   print ( '\nExpected Output: None' + '    ' + 'Output : ' + str ( I1Ii11I1Ii1i . find_ordered ( 0 ) ) )
  except :
   print ( '\nTest failed to run' )
  print ( '\nreverse_list - 5pts' )
  print ( '\nReversing current list' )
  i1111 = I1Ii11I1Ii1i . reverse_list ( )
  i1 = [ ]
  oOOoo00O0O = i1111 . first
  while oOOoo00O0O != None :
   i1 . append ( oOOoo00O0O . data )
   oOOoo00O0O = oOOoo00O0O . next
  try :
   print ( '\nExpected Contents: [7,6,5,4,3,2,1]' + '    ' + 'Contents : ' + str ( i1 ) )
  except :
   print ( '\nTest failed to run' )
  print ( '\nfind_unordered - 5pts' )
  print ( '\nSearching for 4' )
  try :
   print ( '\nExpected Output: 4' + '    ' + 'Output : ' + str ( ( i1111 . find_unordered ( 4 ) ) . data ) )
  except :
   print ( '\nTest failed to run' )
 except :
  print ( '\nInsertion / Reverse / Search Test Failed' )
  if 22 - 22: o00O0oo . IIII
 try :
  print ( '\n\n\nCopy / Equality / Merge / Sort Test (15 pts):' )
  O0O0OO0O0O0 = OO0o ( ooo0OO , inp_f )
  I11 = O0O0OO0O0O0 . LinkedList ( )
  for Ooo in [ 1 , 3 , 5 ] :
   I11 . insert_last ( Ooo )
  Oo0o0000o0o0 = O0O0OO0O0O0 . LinkedList ( )
  for o0oOoO00o in [ 6 , 2 , 4 ] :
   Oo0o0000o0o0 . insert_last ( o0oOoO00o )
  print ( '\nCreating list 1 -> 3 -> 5 and list 6 -> 2 -> 4' )
  print ( '\nCopying list 6 -> 2 -> 4' )
  oOo0oooo00o = Oo0o0000o0o0 . copy_list ( )
  print ( '\nis_equal - 5pts' )
  print ( '\nChecking if original and copy are same' )
  try :
   print ( '\nExpected Output: True' + '    ' + 'Output : ' + str ( oOo0oooo00o . is_equal ( Oo0o0000o0o0 ) ) )
  except :
   print ( '\nTest failed to run' )
  i1111 = I11 . merge_list ( Oo0o0000o0o0 . sort_list ( ) )
  i1 = [ ]
  oOOoo00O0O = i1111 . first
  while oOOoo00O0O != None :
   i1 . append ( oOOoo00O0O . data )
   oOOoo00O0O = oOOoo00O0O . next
  print ( '\nmerge_list / sort_list - 10pts' )
  print ( '\nSorting list 6 -> 2 -> 4 and merging with list 1 -> 3 -> 5' )
  try :
   print ( '\nExpected Contents: [1,2,3,4,5,6]' + '    ' + 'Contents : ' + str ( i1 ) )
  except :
   print ( '\nTest failed to run' )
 except :
  print ( '\nCopy / Equality / Merge / Sort Test Failed' )
  if 65 - 65: iiiiIi11i * OOO0O * o0oO0
 try :
  print ( '\n\n\nDelete / Remove Duplicates Test (15 pts) :' )
  O0O0OO0O0O0 = OO0o ( ooo0OO , inp_f )
  IiI1i = O0O0OO0O0O0 . LinkedList ( )
  for Ooo in [ 0 , 1 , 1 , 2 , 2 , 3 , 3 , 0 ] :
   IiI1i . insert_last ( Ooo )
  OOo0o0 = IiI1i . first
  O0OoOoo00o = IiI1i . delete_link ( 0 )
  print ( '\nCreating list 0 -> 1 -> 1 -> 2 -> 2 -> 3 -> 3 -> 0' )
  print ( '\ndelete_link - 5pts' )
  print ( '\nDeleting 0, and checking identity of returned link' )
  try :
   print ( '\nExpected Deleted Link: ' + str ( OOo0o0 ) + '    ' + 'Deleted Link : ' + str ( O0OoOoo00o ) )
  except :
   print ( '\nTest failed to run' )
  print ( '\nremove_duplicates - 5pts' )
  print ( '\nRemoving duplicates' )
  iiiI11 = IiI1i . remove_duplicates ( )
  i1 = [ ]
  oOOoo00O0O = iiiI11 . first
  while oOOoo00O0O != None :
   i1 . append ( oOOoo00O0O . data )
   oOOoo00O0O = oOOoo00O0O . next
  try :
   print ( '\nExpected Contents: [1,2,3,0]' + '    ' + 'Contents : ' + str ( i1 ) )
  except :
   print ( '\nTest failed to run' )
  print ( '\ndelete_link_2 electric boogaloo - 5pts' )
  print ( '\nDeleting 4, and checking identity of returned link' )
  try :
   print ( '\nExpected Deleted Link: None' + '    ' + 'Deleted Link : ' + str ( iiiI11 . delete_link ( 4 ) ) )
  except :
   print ( '\nTest failed to run' )
 except :
  print ( '\n Delete / Remove Duplicates Test Failed' )
  if 91 - 91: iiiiIi11i / OoO0O00 . iII111i + I1Ii111
def iI11 ( ) :
 iiiii ( 'TestLinkedList.py' )
 if 17 - 17: iiiiIi11i
if __name__ == '__main__' :
 iI11 ( )
 if 64 - 64: o00O0oo % oo % II1Ii
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
