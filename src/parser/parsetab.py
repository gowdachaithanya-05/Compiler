
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftEQNEleftLTLEGTGEleftPLUSMINUSleftMULTIPLYDIVIDErightUMINUSASSIGN COMMA DIVIDE ELSE EQ FLOAT FLOAT_LITERAL GE GT IDENTIFIER IF INT INT_LITERAL LBRACE LE LPAREN LT MINUS MULTIPLY NE PLUS RBRACE RETURN RPAREN SEMICOLONprogram : declarationsdeclarations : declarations declaration\n                    | declarationdeclaration : var_declaration\n                   | func_declarationvar_declaration : type_specifier IDENTIFIER SEMICOLON\n                       | type_specifier IDENTIFIER ASSIGN expression SEMICOLONtype_specifier : INT\n                      | FLOATfunc_declaration : type_specifier IDENTIFIER LPAREN params RPAREN compound_stmtparams : param_list\n              | emptyparam_list : param_list COMMA param\n                  | paramparam : type_specifier IDENTIFIERcompound_stmt : LBRACE stmt_list RBRACEstmt_list : stmt_list statement\n                 | emptystatement : expr_stmt\n                 | var_declaration\n                 | compound_stmt\n                 | if_stmt\n                 | return_stmtif_stmt : IF LPAREN expression RPAREN statement\n               | IF LPAREN expression RPAREN statement ELSE statementreturn_stmt : RETURN expression SEMICOLONexpr_stmt : expression SEMICOLONexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression MULTIPLY expression\n                  | expression DIVIDE expression\n                  | expression LT expression\n                  | expression GT expression\n                  | expression LE expression\n                  | expression GE expression\n                  | expression EQ expression\n                  | expression NE expressionexpression : MINUS expression %prec UMINUSexpression : LPAREN expression RPARENexpression : INT_LITERAL\n                  | FLOAT_LITERALexpression : IDENTIFIERexpression : IDENTIFIER LPAREN arg_list RPARENarg_list : arg_list COMMA expression\n                | expression\n                | emptyempty :'
    
_lr_action_items = {'INT':([0,2,3,4,5,9,11,13,26,41,56,57,61,62,64,65,66,67,68,69,70,75,80,81,82,83,84,],[7,7,-3,-4,-5,-2,-6,7,-7,7,-10,-47,7,-18,-16,-17,-19,-20,-21,-22,-23,-27,-26,7,-24,7,-25,]),'FLOAT':([0,2,3,4,5,9,11,13,26,41,56,57,61,62,64,65,66,67,68,69,70,75,80,81,82,83,84,],[8,8,-3,-4,-5,-2,-6,8,-7,8,-10,-47,8,-18,-16,-17,-19,-20,-21,-22,-23,-27,-26,8,-24,8,-25,]),'$end':([1,2,3,4,5,9,11,26,56,64,],[0,-1,-3,-4,-5,-2,-6,-7,-10,-16,]),'IDENTIFIER':([6,7,8,11,12,16,17,20,25,26,27,28,29,30,31,32,33,34,35,36,57,60,61,62,64,65,66,67,68,69,70,72,74,75,77,80,81,82,83,84,],[10,-8,-9,-6,14,14,14,39,14,-7,14,14,14,14,14,14,14,14,14,14,-47,14,14,-18,-16,-17,-19,-20,-21,-22,-23,76,14,-27,14,-26,14,-24,14,-25,]),'SEMICOLON':([10,14,15,18,19,37,45,46,47,48,49,50,51,52,53,54,55,59,71,76,78,],[11,-42,26,-40,-41,-38,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-39,-43,75,11,80,]),'ASSIGN':([10,76,],[12,12,]),'LPAREN':([10,11,12,14,16,17,25,26,27,28,29,30,31,32,33,34,35,36,57,60,61,62,64,65,66,67,68,69,70,73,74,75,77,80,81,82,83,84,],[13,-6,17,25,17,17,17,-7,17,17,17,17,17,17,17,17,17,17,-47,17,17,-18,-16,-17,-19,-20,-21,-22,-23,77,17,-27,17,-26,17,-24,17,-25,]),'RBRACE':([11,26,57,61,62,64,65,66,67,68,69,70,75,80,82,84,],[-6,-7,-47,64,-18,-16,-17,-19,-20,-21,-22,-23,-27,-26,-24,-25,]),'LBRACE':([11,26,40,57,61,62,64,65,66,67,68,69,70,75,80,81,82,83,84,],[-6,-7,57,-47,57,-18,-16,-17,-19,-20,-21,-22,-23,-27,-26,57,-24,57,-25,]),'IF':([11,26,57,61,62,64,65,66,67,68,69,70,75,80,81,82,83,84,],[-6,-7,-47,73,-18,-16,-17,-19,-20,-21,-22,-23,-27,-26,73,-24,73,-25,]),'RETURN':([11,26,57,61,62,64,65,66,67,68,69,70,75,80,81,82,83,84,],[-6,-7,-47,74,-18,-16,-17,-19,-20,-21,-22,-23,-27,-26,74,-24,74,-25,]),'MINUS':([11,12,14,15,16,17,18,19,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,45,46,47,48,49,50,51,52,53,54,55,57,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,77,78,79,80,81,82,83,84,],[-6,16,-42,28,16,16,-40,-41,16,-7,16,16,16,16,16,16,16,16,16,16,-38,28,28,-28,-29,-30,-31,28,28,28,28,28,28,-39,-47,-43,16,16,-18,28,-16,-17,-19,-20,-21,-22,-23,28,16,-27,16,28,28,-26,16,-24,16,-25,]),'INT_LITERAL':([11,12,16,17,25,26,27,28,29,30,31,32,33,34,35,36,57,60,61,62,64,65,66,67,68,69,70,74,75,77,80,81,82,83,84,],[-6,18,18,18,18,-7,18,18,18,18,18,18,18,18,18,18,-47,18,18,-18,-16,-17,-19,-20,-21,-22,-23,18,-27,18,-26,18,-24,18,-25,]),'FLOAT_LITERAL':([11,12,16,17,25,26,27,28,29,30,31,32,33,34,35,36,57,60,61,62,64,65,66,67,68,69,70,74,75,77,80,81,82,83,84,],[-6,19,19,19,19,-7,19,19,19,19,19,19,19,19,19,19,-47,19,19,-18,-16,-17,-19,-20,-21,-22,-23,19,-27,19,-26,19,-24,19,-25,]),'ELSE':([11,26,64,66,67,68,69,70,75,80,82,84,],[-6,-7,-16,-19,-20,-21,-22,-23,-27,-26,83,-25,]),'RPAREN':([13,14,18,19,21,22,23,24,25,37,38,39,42,43,44,45,46,47,48,49,50,51,52,53,54,55,58,59,63,79,],[-47,-42,-40,-41,40,-11,-12,-14,-47,-38,55,-15,59,-45,-46,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-39,-13,-43,-44,81,]),'PLUS':([14,15,18,19,37,38,43,45,46,47,48,49,50,51,52,53,54,55,59,63,71,78,79,],[-42,27,-40,-41,-38,27,27,-28,-29,-30,-31,27,27,27,27,27,27,-39,-43,27,27,27,27,]),'MULTIPLY':([14,15,18,19,37,38,43,45,46,47,48,49,50,51,52,53,54,55,59,63,71,78,79,],[-42,29,-40,-41,-38,29,29,29,29,-30,-31,29,29,29,29,29,29,-39,-43,29,29,29,29,]),'DIVIDE':([14,15,18,19,37,38,43,45,46,47,48,49,50,51,52,53,54,55,59,63,71,78,79,],[-42,30,-40,-41,-38,30,30,30,30,-30,-31,30,30,30,30,30,30,-39,-43,30,30,30,30,]),'LT':([14,15,18,19,37,38,43,45,46,47,48,49,50,51,52,53,54,55,59,63,71,78,79,],[-42,31,-40,-41,-38,31,31,-28,-29,-30,-31,-32,-33,-34,-35,31,31,-39,-43,31,31,31,31,]),'GT':([14,15,18,19,37,38,43,45,46,47,48,49,50,51,52,53,54,55,59,63,71,78,79,],[-42,32,-40,-41,-38,32,32,-28,-29,-30,-31,-32,-33,-34,-35,32,32,-39,-43,32,32,32,32,]),'LE':([14,15,18,19,37,38,43,45,46,47,48,49,50,51,52,53,54,55,59,63,71,78,79,],[-42,33,-40,-41,-38,33,33,-28,-29,-30,-31,-32,-33,-34,-35,33,33,-39,-43,33,33,33,33,]),'GE':([14,15,18,19,37,38,43,45,46,47,48,49,50,51,52,53,54,55,59,63,71,78,79,],[-42,34,-40,-41,-38,34,34,-28,-29,-30,-31,-32,-33,-34,-35,34,34,-39,-43,34,34,34,34,]),'EQ':([14,15,18,19,37,38,43,45,46,47,48,49,50,51,52,53,54,55,59,63,71,78,79,],[-42,35,-40,-41,-38,35,35,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-39,-43,35,35,35,35,]),'NE':([14,15,18,19,37,38,43,45,46,47,48,49,50,51,52,53,54,55,59,63,71,78,79,],[-42,36,-40,-41,-38,36,36,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-39,-43,36,36,36,36,]),'COMMA':([14,18,19,22,24,25,37,39,42,43,44,45,46,47,48,49,50,51,52,53,54,55,58,59,63,],[-42,-40,-41,41,-14,-47,-38,-15,60,-45,-46,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-39,-13,-43,-44,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declarations':([0,],[2,]),'declaration':([0,2,],[3,9,]),'var_declaration':([0,2,61,81,83,],[4,4,67,67,67,]),'func_declaration':([0,2,],[5,5,]),'type_specifier':([0,2,13,41,61,81,83,],[6,6,20,20,72,72,72,]),'expression':([12,16,17,25,27,28,29,30,31,32,33,34,35,36,60,61,74,77,81,83,],[15,37,38,43,45,46,47,48,49,50,51,52,53,54,63,71,78,79,71,71,]),'params':([13,],[21,]),'param_list':([13,],[22,]),'empty':([13,25,57,],[23,44,62,]),'param':([13,41,],[24,58,]),'arg_list':([25,],[42,]),'compound_stmt':([40,61,81,83,],[56,68,68,68,]),'stmt_list':([57,],[61,]),'statement':([61,81,83,],[65,82,84,]),'expr_stmt':([61,81,83,],[66,66,66,]),'if_stmt':([61,81,83,],[69,69,69,]),'return_stmt':([61,81,83,],[70,70,70,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declarations','program',1,'p_program','parser.py',32),
  ('declarations -> declarations declaration','declarations',2,'p_declarations','parser.py',37),
  ('declarations -> declaration','declarations',1,'p_declarations','parser.py',38),
  ('declaration -> var_declaration','declaration',1,'p_declaration','parser.py',45),
  ('declaration -> func_declaration','declaration',1,'p_declaration','parser.py',46),
  ('var_declaration -> type_specifier IDENTIFIER SEMICOLON','var_declaration',3,'p_var_declaration','parser.py',50),
  ('var_declaration -> type_specifier IDENTIFIER ASSIGN expression SEMICOLON','var_declaration',5,'p_var_declaration','parser.py',51),
  ('type_specifier -> INT','type_specifier',1,'p_type_specifier','parser.py',61),
  ('type_specifier -> FLOAT','type_specifier',1,'p_type_specifier','parser.py',62),
  ('func_declaration -> type_specifier IDENTIFIER LPAREN params RPAREN compound_stmt','func_declaration',6,'p_func_declaration','parser.py',66),
  ('params -> param_list','params',1,'p_params','parser.py',74),
  ('params -> empty','params',1,'p_params','parser.py',75),
  ('param_list -> param_list COMMA param','param_list',3,'p_param_list','parser.py',79),
  ('param_list -> param','param_list',1,'p_param_list','parser.py',80),
  ('param -> type_specifier IDENTIFIER','param',2,'p_param','parser.py',87),
  ('compound_stmt -> LBRACE stmt_list RBRACE','compound_stmt',3,'p_compound_stmt','parser.py',93),
  ('stmt_list -> stmt_list statement','stmt_list',2,'p_stmt_list','parser.py',97),
  ('stmt_list -> empty','stmt_list',1,'p_stmt_list','parser.py',98),
  ('statement -> expr_stmt','statement',1,'p_statement','parser.py',105),
  ('statement -> var_declaration','statement',1,'p_statement','parser.py',106),
  ('statement -> compound_stmt','statement',1,'p_statement','parser.py',107),
  ('statement -> if_stmt','statement',1,'p_statement','parser.py',108),
  ('statement -> return_stmt','statement',1,'p_statement','parser.py',109),
  ('if_stmt -> IF LPAREN expression RPAREN statement','if_stmt',5,'p_if_stmt','parser.py',113),
  ('if_stmt -> IF LPAREN expression RPAREN statement ELSE statement','if_stmt',7,'p_if_stmt','parser.py',114),
  ('return_stmt -> RETURN expression SEMICOLON','return_stmt',3,'p_return_stmt','parser.py',121),
  ('expr_stmt -> expression SEMICOLON','expr_stmt',2,'p_expr_stmt','parser.py',126),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',130),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',131),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression_binop','parser.py',132),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser.py',133),
  ('expression -> expression LT expression','expression',3,'p_expression_binop','parser.py',134),
  ('expression -> expression GT expression','expression',3,'p_expression_binop','parser.py',135),
  ('expression -> expression LE expression','expression',3,'p_expression_binop','parser.py',136),
  ('expression -> expression GE expression','expression',3,'p_expression_binop','parser.py',137),
  ('expression -> expression EQ expression','expression',3,'p_expression_binop','parser.py',138),
  ('expression -> expression NE expression','expression',3,'p_expression_binop','parser.py',139),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','parser.py',146),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',151),
  ('expression -> INT_LITERAL','expression',1,'p_expression_number','parser.py',155),
  ('expression -> FLOAT_LITERAL','expression',1,'p_expression_number','parser.py',156),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','parser.py',160),
  ('expression -> IDENTIFIER LPAREN arg_list RPAREN','expression',4,'p_expression_call','parser.py',164),
  ('arg_list -> arg_list COMMA expression','arg_list',3,'p_arg_list','parser.py',168),
  ('arg_list -> expression','arg_list',1,'p_arg_list','parser.py',169),
  ('arg_list -> empty','arg_list',1,'p_arg_list','parser.py',170),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',182),
]
