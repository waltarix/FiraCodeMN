select(.Name != "Material legacy")
|
"Patch(
      name=\(.Name | @sh),
      filename=\(.Filename | split("/")[-1] | @sh),
      sym_start=\(.SymStart),
      sym_end=\(.SymEnd),
      src_start=\(.SrcStart // "None"),
      exact=\(if .Exact then "True" else "False" end),
),"
