
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftEQNEleftLTLEGTGEleftPLUSMINUSleftMULTIPLYDIVIDErightUMINUSASSIGN COMMA DIVIDE ELSE EQ FLOAT FLOAT_LITERAL GE GT IDENTIFIER IF INT INT_LITERAL LBRACE LE LPAREN LT MINUS MULTIPLY NE PLUS RBRACE RETURN RPAREN SEMICOLON WHILEprogram : declarationsdeclarations : declarations declaration\n                    | declarationdeclaration : var_declaration\n                   | func_declarationvar_declaration : type_specifier IDENTIFIER SEMICOLON\n                       | type_specifier IDENTIFIER ASSIGN expression SEMICOLONtype_specifier : INT\n                      | FLOATfunc_declaration : type_specifier IDENTIFIER LPAREN params RPAREN compound_stmtparams : param_list\n              | emptyparam_list : param_list COMMA param\n                  | paramparam : type_specifier IDENTIFIERcompound_stmt : LBRACE stmt_list RBRACEstmt_list : stmt_list statement\n                 | emptystatement : expr_stmt\n                 | var_declaration\n                 | compound_stmt\n                 | if_stmt\n                 | return_stmtif_stmt : IF LPAREN expression RPAREN statement\n               | IF LPAREN expression RPAREN statement ELSE statementreturn_stmt : RETURN expression SEMICOLONexpr_stmt : expression SEMICOLONexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression MULTIPLY expression\n                  | expression DIVIDE expression\n                  | expression LT expression\n                  | expression GT expression\n                  | expression LE expression\n                  | expression GE expression\n                  | expression EQ expression\n                  | expression NE expressionexpression : MINUS expression %prec UMINUSexpression : LPAREN expression RPARENexpression : INT_LITERAL\n                  | FLOAT_LITERALexpression : IDENTIFIERempty :'
    
_lr_action_items = {'INT':([0,2,3,4,5,9,11,13,25,40,52,53,55,56,57,58,59,60,61,62,63,68,73,74,75,76,77,],[7,7,-3,-4,-5,-2,-6,7,-7,7,-10,-43,7,-18,-16,-17,-19,-20,-21,-22,-23,-27,-26,7,-24,7,-25,]),'FLOAT':([0,2,3,4,5,9,11,13,25,40,52,53,55,56,57,58,59,60,61,62,63,68,73,74,75,76,77,],[8,8,-3,-4,-5,-2,-6,8,-7,8,-10,-43,8,-18,-16,-17,-19,-20,-21,-22,-23,-27,-26,8,-24,8,-25,]),'$end':([1,2,3,4,5,9,11,25,52,57,],[0,-1,-3,-4,-5,-2,-6,-7,-10,-16,]),'IDENTIFIER':([6,7,8,11,12,16,17,20,25,26,27,28,29,30,31,32,33,34,35,53,55,56,57,58,59,60,61,62,63,65,67,68,70,73,74,75,76,77,],[10,-8,-9,-6,14,14,14,38,-7,14,14,14,14,14,14,14,14,14,14,-43,14,-18,-16,-17,-19,-20,-21,-22,-23,69,14,-27,14,-26,14,-24,14,-25,]),'SEMICOLON':([10,14,15,18,19,36,41,42,43,44,45,46,47,48,49,50,51,64,69,71,],[11,-42,25,-40,-41,-38,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-39,68,11,73,]),'ASSIGN':([10,69,],[12,12,]),'LPAREN':([10,11,12,16,17,25,26,27,28,29,30,31,32,33,34,35,53,55,56,57,58,59,60,61,62,63,66,67,68,70,73,74,75,76,77,],[13,-6,17,17,17,-7,17,17,17,17,17,17,17,17,17,17,-43,17,-18,-16,-17,-19,-20,-21,-22,-23,70,17,-27,17,-26,17,-24,17,-25,]),'RBRACE':([11,25,53,55,56,57,58,59,60,61,62,63,68,73,75,77,],[-6,-7,-43,57,-18,-16,-17,-19,-20,-21,-22,-23,-27,-26,-24,-25,]),'LBRACE':([11,25,39,53,55,56,57,58,59,60,61,62,63,68,73,74,75,76,77,],[-6,-7,53,-43,53,-18,-16,-17,-19,-20,-21,-22,-23,-27,-26,53,-24,53,-25,]),'IF':([11,25,53,55,56,57,58,59,60,61,62,63,68,73,74,75,76,77,],[-6,-7,-43,66,-18,-16,-17,-19,-20,-21,-22,-23,-27,-26,66,-24,66,-25,]),'RETURN':([11,25,53,55,56,57,58,59,60,61,62,63,68,73,74,75,76,77,],[-6,-7,-43,67,-18,-16,-17,-19,-20,-21,-22,-23,-27,-26,67,-24,67,-25,]),'MINUS':([11,12,14,15,16,17,18,19,25,26,27,28,29,30,31,32,33,34,35,36,37,41,42,43,44,45,46,47,48,49,50,51,53,55,56,57,58,59,60,61,62,63,64,67,68,70,71,72,73,74,75,76,77,],[-6,16,-42,27,16,16,-40,-41,-7,16,16,16,16,16,16,16,16,16,16,-38,27,-28,-29,-30,-31,27,27,27,27,27,27,-39,-43,16,-18,-16,-17,-19,-20,-21,-22,-23,27,16,-27,16,27,27,-26,16,-24,16,-25,]),'INT_LITERAL':([11,12,16,17,25,26,27,28,29,30,31,32,33,34,35,53,55,56,57,58,59,60,61,62,63,67,68,70,73,74,75,76,77,],[-6,18,18,18,-7,18,18,18,18,18,18,18,18,18,18,-43,18,-18,-16,-17,-19,-20,-21,-22,-23,18,-27,18,-26,18,-24,18,-25,]),'FLOAT_LITERAL':([11,12,16,17,25,26,27,28,29,30,31,32,33,34,35,53,55,56,57,58,59,60,61,62,63,67,68,70,73,74,75,76,77,],[-6,19,19,19,-7,19,19,19,19,19,19,19,19,19,19,-43,19,-18,-16,-17,-19,-20,-21,-22,-23,19,-27,19,-26,19,-24,19,-25,]),'ELSE':([11,25,57,59,60,61,62,63,68,73,75,77,],[-6,-7,-16,-19,-20,-21,-22,-23,-27,-26,76,-25,]),'RPAREN':([13,14,18,19,21,22,23,24,36,37,38,41,42,43,44,45,46,47,48,49,50,51,54,72,],[-43,-42,-40,-41,39,-11,-12,-14,-38,51,-15,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-39,-13,74,]),'PLUS':([14,15,18,19,36,37,41,42,43,44,45,46,47,48,49,50,51,64,71,72,],[-42,26,-40,-41,-38,26,-28,-29,-30,-31,26,26,26,26,26,26,-39,26,26,26,]),'MULTIPLY':([14,15,18,19,36,37,41,42,43,44,45,46,47,48,49,50,51,64,71,72,],[-42,28,-40,-41,-38,28,28,28,-30,-31,28,28,28,28,28,28,-39,28,28,28,]),'DIVIDE':([14,15,18,19,36,37,41,42,43,44,45,46,47,48,49,50,51,64,71,72,],[-42,29,-40,-41,-38,29,29,29,-30,-31,29,29,29,29,29,29,-39,29,29,29,]),'LT':([14,15,18,19,36,37,41,42,43,44,45,46,47,48,49,50,51,64,71,72,],[-42,30,-40,-41,-38,30,-28,-29,-30,-31,-32,-33,-34,-35,30,30,-39,30,30,30,]),'GT':([14,15,18,19,36,37,41,42,43,44,45,46,47,48,49,50,51,64,71,72,],[-42,31,-40,-41,-38,31,-28,-29,-30,-31,-32,-33,-34,-35,31,31,-39,31,31,31,]),'LE':([14,15,18,19,36,37,41,42,43,44,45,46,47,48,49,50,51,64,71,72,],[-42,32,-40,-41,-38,32,-28,-29,-30,-31,-32,-33,-34,-35,32,32,-39,32,32,32,]),'GE':([14,15,18,19,36,37,41,42,43,44,45,46,47,48,49,50,51,64,71,72,],[-42,33,-40,-41,-38,33,-28,-29,-30,-31,-32,-33,-34,-35,33,33,-39,33,33,33,]),'EQ':([14,15,18,19,36,37,41,42,43,44,45,46,47,48,49,50,51,64,71,72,],[-42,34,-40,-41,-38,34,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-39,34,34,34,]),'NE':([14,15,18,19,36,37,41,42,43,44,45,46,47,48,49,50,51,64,71,72,],[-42,35,-40,-41,-38,35,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-39,35,35,35,]),'COMMA':([22,24,38,54,],[40,-14,-15,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declarations':([0,],[2,]),'declaration':([0,2,],[3,9,]),'var_declaration':([0,2,55,74,76,],[4,4,60,60,60,]),'func_declaration':([0,2,],[5,5,]),'type_specifier':([0,2,13,40,55,74,76,],[6,6,20,20,65,65,65,]),'expression':([12,16,17,26,27,28,29,30,31,32,33,34,35,55,67,70,74,76,],[15,36,37,41,42,43,44,45,46,47,48,49,50,64,71,72,64,64,]),'params':([13,],[21,]),'param_list':([13,],[22,]),'empty':([13,53,],[23,56,]),'param':([13,40,],[24,54,]),'compound_stmt':([39,55,74,76,],[52,61,61,61,]),'stmt_list':([53,],[55,]),'statement':([55,74,76,],[58,75,77,]),'expr_stmt':([55,74,76,],[59,59,59,]),'if_stmt':([55,74,76,],[62,62,62,]),'return_stmt':([55,74,76,],[63,63,63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declarations','program',1,'p_program','parser.py',31),
  ('declarations -> declarations declaration','declarations',2,'p_declarations','parser.py',36),
  ('declarations -> declaration','declarations',1,'p_declarations','parser.py',37),
  ('declaration -> var_declaration','declaration',1,'p_declaration','parser.py',44),
  ('declaration -> func_declaration','declaration',1,'p_declaration','parser.py',45),
  ('var_declaration -> type_specifier IDENTIFIER SEMICOLON','var_declaration',3,'p_var_declaration','parser.py',49),
  ('var_declaration -> type_specifier IDENTIFIER ASSIGN expression SEMICOLON','var_declaration',5,'p_var_declaration','parser.py',50),
  ('type_specifier -> INT','type_specifier',1,'p_type_specifier','parser.py',60),
  ('type_specifier -> FLOAT','type_specifier',1,'p_type_specifier','parser.py',61),
  ('func_declaration -> type_specifier IDENTIFIER LPAREN params RPAREN compound_stmt','func_declaration',6,'p_func_declaration','parser.py',65),
  ('params -> param_list','params',1,'p_params','parser.py',73),
  ('params -> empty','params',1,'p_params','parser.py',74),
  ('param_list -> param_list COMMA param','param_list',3,'p_param_list','parser.py',78),
  ('param_list -> param','param_list',1,'p_param_list','parser.py',79),
  ('param -> type_specifier IDENTIFIER','param',2,'p_param','parser.py',86),
  ('compound_stmt -> LBRACE stmt_list RBRACE','compound_stmt',3,'p_compound_stmt','parser.py',92),
  ('stmt_list -> stmt_list statement','stmt_list',2,'p_stmt_list','parser.py',96),
  ('stmt_list -> empty','stmt_list',1,'p_stmt_list','parser.py',97),
  ('statement -> expr_stmt','statement',1,'p_statement','parser.py',104),
  ('statement -> var_declaration','statement',1,'p_statement','parser.py',105),
  ('statement -> compound_stmt','statement',1,'p_statement','parser.py',106),
  ('statement -> if_stmt','statement',1,'p_statement','parser.py',107),
  ('statement -> return_stmt','statement',1,'p_statement','parser.py',108),
  ('if_stmt -> IF LPAREN expression RPAREN statement','if_stmt',5,'p_if_stmt','parser.py',112),
  ('if_stmt -> IF LPAREN expression RPAREN statement ELSE statement','if_stmt',7,'p_if_stmt','parser.py',113),
  ('return_stmt -> RETURN expression SEMICOLON','return_stmt',3,'p_return_stmt','parser.py',120),
  ('expr_stmt -> expression SEMICOLON','expr_stmt',2,'p_expr_stmt','parser.py',125),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',129),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',130),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression_binop','parser.py',131),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser.py',132),
  ('expression -> expression LT expression','expression',3,'p_expression_binop','parser.py',133),
  ('expression -> expression GT expression','expression',3,'p_expression_binop','parser.py',134),
  ('expression -> expression LE expression','expression',3,'p_expression_binop','parser.py',135),
  ('expression -> expression GE expression','expression',3,'p_expression_binop','parser.py',136),
  ('expression -> expression EQ expression','expression',3,'p_expression_binop','parser.py',137),
  ('expression -> expression NE expression','expression',3,'p_expression_binop','parser.py',138),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','parser.py',145),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',150),
  ('expression -> INT_LITERAL','expression',1,'p_expression_number','parser.py',154),
  ('expression -> FLOAT_LITERAL','expression',1,'p_expression_number','parser.py',155),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','parser.py',159),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',163),
]
