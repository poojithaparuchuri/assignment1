"""
    Sree Poojitha
    File : dynamic_protocol.py
"""
# !/usr/bin/python

def main():
    """
    calculate the volumes of NaCl and
    MgCl2 stock solutions required to make a desired solution
    and provides a protocol for preparation.
    """
    final_sol_vol_ml = float(input('Please enter the final volume of the solution (ml): '))
    nacl_stock_conc_mm = float(input('Please enter the NaCl stock (mM): '))
    final_nacl_conc_mm = float(input('Please enter the NaCl final (mM): '))
    mgcl2_stock_conc_mm = float(input('Please enter the MgCl2 stock (mM): '))
    final_mgcl2_conc_mm = float(input('Please enter the MgCl2 final (mM): '))

    # Calculate the volumes of stock solutions required
    volume_nacl_stock_ml = ((final_sol_vol_ml * final_nacl_conc_mm)
                            / nacl_stock_conc_mm)
    volume_mgcl2_stock_ml = ((final_sol_vol_ml * final_mgcl2_conc_mm)
                             / mgcl2_stock_conc_mm)

    # Create a protocol
    protocol_dynamic = f"Add {volume_nacl_stock_ml:.2f} ml NaCl\n"
    protocol_dynamic += f"Add {volume_mgcl2_stock_ml:.3f} ml MgCl2\n"
    protocol_dynamic += f"Add water to a final volume of {final_sol_vol_ml:.1f} ml and mix"

    # Print the protocol
    print(protocol_dynamic)

if __name__ == "__main__":
    main()
