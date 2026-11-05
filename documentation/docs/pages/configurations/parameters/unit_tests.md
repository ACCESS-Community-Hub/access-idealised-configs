---
search:
  exclude: true
---

# unit_tests: MOM_parameter_doc.all

Every MOM6 parameter of the tested run of [unit_tests](../mom6examples/unit_tests.md), as MOM6 wrote it to `MOM_parameter_doc.all` in the run's output folder. Line numbers match the file.

<pre class="paramdoc"><span id="L1">! This file was written by the model and records all non-layout or debugging parameters used at run-time.</span>
<span id="L2"></span>
<span id="L3">! === module MOM ===</span>
<span id="L4">SPLIT = False                   !   [Boolean] default = True</span>
<span id="L5">                                ! Use the split time stepping if true.</span>
<span id="L6">USE_RK2 = False                 !   [Boolean] default = False</span>
<span id="L7">                                ! If true, use RK2 instead of RK3 in the unsplit time stepping.</span>
<span id="L8">CALC_RHO_FOR_SEA_LEVEL = False  !   [Boolean] default = False</span>
<span id="L9">                                ! If true, the in-situ density is used to calculate the effective sea level that</span>
<span id="L10">                                ! is returned to the coupler. If false, the Boussinesq parameter RHO_0 is used.</span>
<span id="L11">ENABLE_THERMODYNAMICS = False   !   [Boolean] default = True</span>
<span id="L12">                                ! If true, Temperature and salinity are used as state variables.</span>
<span id="L13">USE_EOS = False                 !   [Boolean] default = False</span>
<span id="L14">                                ! If true,  density is calculated from temperature and salinity with an equation</span>
<span id="L15">                                ! of state.  If USE_EOS is true, ENABLE_THERMODYNAMICS must be true as well.</span>
<span id="L16">DIABATIC_FIRST = False          !   [Boolean] default = False</span>
<span id="L17">                                ! If true, apply diabatic and thermodynamic processes, including buoyancy</span>
<span id="L18">                                ! forcing and mass gain or loss, before stepping the dynamics forward.</span>
<span id="L19">USE_CONTEMP_ABSSAL = False      !   [Boolean] default = False</span>
<span id="L20">                                ! If true, the prognostics T&amp;S are the conservative temperature and absolute</span>
<span id="L21">                                ! salinity. Care should be taken to convert them to potential temperature and</span>
<span id="L22">                                ! practical salinity before exchanging them with the coupler and/or reporting</span>
<span id="L23">                                ! T&amp;S diagnostics.</span>
<span id="L24">ADIABATIC = True                !   [Boolean] default = False</span>
<span id="L25">                                ! There are no diapycnal mass fluxes if ADIABATIC is true.  This assumes that KD</span>
<span id="L26">                                ! = 0.0 and that there is no buoyancy forcing, but makes the model faster by</span>
<span id="L27">                                ! eliminating subroutine calls.</span>
<span id="L28">DO_DYNAMICS = True              !   [Boolean] default = True</span>
<span id="L29">                                ! If False, skips the dynamics calls that update u &amp; v, as well as the gravity</span>
<span id="L30">                                ! wave adjustment to h. This may be a fragile feature, but can be useful during</span>
<span id="L31">                                ! development</span>
<span id="L32">OFFLINE_TRACER_MODE = False     !   [Boolean] default = False</span>
<span id="L33">                                ! If true, barotropic and baroclinic dynamics, thermodynamics are all bypassed</span>
<span id="L34">                                ! with all the fields necessary to integrate the tracer advection and diffusion</span>
<span id="L35">                                ! equation are read in from files stored from a previous integration of the</span>
<span id="L36">                                ! prognostic model. NOTE: This option only used in the ocean_solo_driver.</span>
<span id="L37">USE_REGRIDDING = False          !   [Boolean] default = False</span>
<span id="L38">                                ! If True, use the ALE algorithm (regridding/remapping). If False, use the</span>
<span id="L39">                                ! layered isopycnal algorithm.</span>
<span id="L40">BULKMIXEDLAYER = False          !   [Boolean] default = False</span>
<span id="L41">                                ! If true, use a Kraus-Turner-like bulk mixed layer with transitional buffer</span>
<span id="L42">                                ! layers.  Layers 1 through NKML+NKBL have variable densities. There must be at</span>
<span id="L43">                                ! least NKML+NKBL+1 layers if BULKMIXEDLAYER is true. BULKMIXEDLAYER can not be</span>
<span id="L44">                                ! used with USE_REGRIDDING. The default is influenced by ENABLE_THERMODYNAMICS.</span>
<span id="L45">USE_POROUS_BARRIER = False      !   [Boolean] default = False</span>
<span id="L46">                                ! If true, use porous barrier to constrain the widths and face areas at the</span>
<span id="L47">                                ! edges of the grid cells.</span>
<span id="L48">BATHYMETRY_AT_VEL = False       !   [Boolean] default = False</span>
<span id="L49">                                ! If true, there are separate values for the basin depths at velocity points.</span>
<span id="L50">                                ! Otherwise the effects of topography are entirely determined from thickness</span>
<span id="L51">                                ! points.</span>
<span id="L52">ENABLE_BUGS_BY_DEFAULT = True   !   [Boolean] default = True</span>
<span id="L53">                                ! If true, the defaults for certain recently added bug-fix flags are set to</span>
<span id="L54">                                ! recreate the bugs so that the code can be moved forward without changing</span>
<span id="L55">                                ! answers for existing configurations.  The defaults for groups of bug-fix flags</span>
<span id="L56">                                ! are periodcially changed to correct the bugs, at which point this parameter</span>
<span id="L57">                                ! will no longer be used to set their default.  Setting this to false means that</span>
<span id="L58">                                ! bugs are only used if they are actively selected, but it also means that</span>
<span id="L59">                                ! answers may change when code is updated due to newly found bugs.</span>
<span id="L60">DT = 8.64E+04                   !   [s]</span>
<span id="L61">                                ! The (baroclinic) dynamics time step.  The time-step that is actually used will</span>
<span id="L62">                                ! be an integer fraction of the forcing time-step (DT_FORCING in ocean-only mode</span>
<span id="L63">                                ! or the coupling timestep in coupled mode.)</span>
<span id="L64">DT_THERM = 8.64E+04             !   [s] default = 8.64E+04</span>
<span id="L65">                                ! The thermodynamic time step. Ideally DT_THERM should be an integer multiple of</span>
<span id="L66">                                ! DT and of DT_TRACER_ADVECT and less than the forcing or coupling time-step.</span>
<span id="L67">                                ! However, if THERMO_SPANS_COUPLING is true, DT_THERM can be an integer multiple</span>
<span id="L68">                                ! of the coupling timestep. By default DT_THERM is set to DT.</span>
<span id="L69">THERMO_SPANS_COUPLING = False   !   [Boolean] default = False</span>
<span id="L70">                                ! If true, the MOM will take thermodynamic timesteps that can be longer than the</span>
<span id="L71">                                ! coupling timestep. The actual thermodynamic timestep that is used in this case</span>
<span id="L72">                                ! is the largest integer multiple of the coupling timestep that is less than or</span>
<span id="L73">                                ! equal to DT_THERM.</span>
<span id="L74">DT_TRACER_ADVECT = 8.64E+04     !   [s] default = 8.64E+04</span>
<span id="L75">                                ! The tracer advection time step. Ideally DT_TRACER_ADVECT should be an integer</span>
<span id="L76">                                ! multiple of DT, less than DT_THERM, and less than the forcing or coupling</span>
<span id="L77">                                ! time-step. However, if TRADV_SPANS_COUPLING is true, DT_TRACER_ADVECT can be</span>
<span id="L78">                                ! longer than the coupling timestep. By default DT_TRACER_ADVECT is set to</span>
<span id="L79">                                ! DT_THERM.</span>
<span id="L80">TRADV_SPANS_COUPLING = False    !   [Boolean] default = False</span>
<span id="L81">                                ! If true, the MOM will take tracer advection timesteps that can be longer than</span>
<span id="L82">                                ! the coupling timestep. The actual tracer advection timestep that is used in</span>
<span id="L83">                                ! this case is the largest integer multiple of the coupling timestep that is</span>
<span id="L84">                                ! less than or equal to DT_TRACER_ADVECT.</span>
<span id="L85">THICKNESSDIFFUSE = False        !   [Boolean] default = False</span>
<span id="L86">                                ! If true, isopycnal surfaces are diffused with a Laplacian coefficient of KHTH.</span>
<span id="L87">APPLY_INTERFACE_FILTER = False  !   [Boolean] default = False</span>
<span id="L88">                                ! If true, model interface heights are subjected to a grid-scale dependent</span>
<span id="L89">                                ! spatial smoothing, often with biharmonic filter.</span>
<span id="L90">HMIX_SFC_PROP = 1.0             !   [m] default = 1.0</span>
<span id="L91">                                ! If BULKMIXEDLAYER is false, HMIX_SFC_PROP is the depth over which to average</span>
<span id="L92">                                ! to find surface properties like SST and SSS or density (but not surface</span>
<span id="L93">                                ! velocities).</span>
<span id="L94">HMIX_UV_SFC_PROP = 0.0          !   [m] default = 0.0</span>
<span id="L95">                                ! If BULKMIXEDLAYER is false, HMIX_UV_SFC_PROP is the depth over which to</span>
<span id="L96">                                ! average to find surface flow properties, SSU, SSV. A non-positive value</span>
<span id="L97">                                ! indicates no averaging.</span>
<span id="L98">HFREEZE = -1.0                  !   [m] default = -1.0</span>
<span id="L99">                                ! If HFREEZE &gt; 0, melt potential will be computed. The actual depth over which</span>
<span id="L100">                                ! melt potential is computed will be min(HFREEZE, OBLD), where OBLD is the</span>
<span id="L101">                                ! boundary layer depth. If HFREEZE &lt;= 0 (default), melt potential will not be</span>
<span id="L102">                                ! computed.</span>
<span id="L103">INTERPOLATE_P_SURF = False      !   [Boolean] default = False</span>
<span id="L104">                                ! If true, linearly interpolate the surface pressure over the coupling time</span>
<span id="L105">                                ! step, using the specified value at the end of the step.</span>
<span id="L106">FIRST_DIRECTION = 0             ! default = 0</span>
<span id="L107">                                ! An integer that indicates which direction goes first in parts of the code that</span>
<span id="L108">                                ! use directionally split updates, with even numbers (or 0) used for x- first</span>
<span id="L109">                                ! and odd numbers used for y-first.</span>
<span id="L110">ALTERNATE_FIRST_DIRECTION = False !   [Boolean] default = False</span>
<span id="L111">                                ! If true, after every dynamic timestep alternate whether the x- or y- direction</span>
<span id="L112">                                ! updates occur first in directionally split parts of the calculation. If this</span>
<span id="L113">                                ! is true, FIRST_DIRECTION applies at the start of a new run or if the next</span>
<span id="L114">                                ! first direction can not be found in the restart file.</span>
<span id="L115">CHECK_BAD_SURFACE_VALS = False  !   [Boolean] default = False</span>
<span id="L116">                                ! If true, check the surface state for ridiculous values.</span>
<span id="L117">DEFAULT_ANSWER_DATE = 20181231  ! default = 99991231</span>
<span id="L118">                                ! This sets the default value for the various _ANSWER_DATE parameters.</span>
<span id="L119">SURFACE_ANSWER_DATE = 20181231  ! default = 20181231</span>
<span id="L120">                                ! The vintage of the expressions for the surface properties.  Values below</span>
<span id="L121">                                ! 20190101 recover the answers from the end of 2018, while higher values use</span>
<span id="L122">                                ! updated and more robust forms of the same expressions.</span>
<span id="L123">SAVE_INITIAL_CONDS = False      !   [Boolean] default = False</span>
<span id="L124">                                ! If true, write the initial conditions to a file given by IC_OUTPUT_FILE.</span>
<span id="L125">IC_OUTPUT_FILE = &quot;MOM_IC&quot;       ! default = &quot;MOM_IC&quot;</span>
<span id="L126">                                ! The file into which to write the initial conditions.</span>
<span id="L127">WRITE_GEOM = 1                  ! default = 1</span>
<span id="L128">                                ! If =0, never write the geometry and vertical grid files. If =1, write the</span>
<span id="L129">                                ! geometry and vertical grid files only for a new simulation. If =2, always</span>
<span id="L130">                                ! write the geometry and vertical grid files. Other values are invalid.</span>
<span id="L131">GEOM_FILE = &quot;ocean_geometry&quot;    ! default = &quot;ocean_geometry&quot;</span>
<span id="L132">                                ! The file into which to write the ocean geometry.</span>
<span id="L133">USE_DBCLIENT = False            !   [Boolean] default = False</span>
<span id="L134">                                ! If true, initialize a client to a remote database that can be used for online</span>
<span id="L135">                                ! analysis and machine-learning inference.</span>
<span id="L136">ICE_SHELF = False               !   [Boolean] default = False</span>
<span id="L137">                                ! If true, enables the ice shelf model.</span>
<span id="L138">USE_PARTICLES = False           !   [Boolean] default = False</span>
<span id="L139">                                ! If true, use the particles package.</span>
<span id="L140">USE_UH_PARTICLES = False        !   [Boolean] default = False</span>
<span id="L141">                                ! If true, use the uh velocity in the particles package.</span>
<span id="L142">ENSEMBLE_OCEAN = False          !   [Boolean] default = False</span>
<span id="L143">                                ! If False, The model is being run in serial mode as a single realization. If</span>
<span id="L144">                                ! True, The current model realization is part of a larger ensemble and at the</span>
<span id="L145">                                ! end of step MOM, we will perform a gather of the ensemble members for</span>
<span id="L146">                                ! statistical evaluation and/or data assimilation.</span>
<span id="L147">HOMOGENIZE_FORCINGS = False     !   [Boolean] default = False</span>
<span id="L148">                                ! If True, homogenize the forces and fluxes.</span>
<span id="L149"></span>
<span id="L150">! === module MOM_domains ===</span>
<span id="L151">REENTRANT_X = True              !   [Boolean] default = True</span>
<span id="L152">                                ! If true, the domain is zonally reentrant.</span>
<span id="L153">REENTRANT_Y = False             !   [Boolean] default = False</span>
<span id="L154">                                ! If true, the domain is meridionally reentrant.</span>
<span id="L155">TRIPOLAR_N = False              !   [Boolean] default = False</span>
<span id="L156">                                ! Use tripolar connectivity at the northern edge of the domain.  With</span>
<span id="L157">                                ! TRIPOLAR_N, NIGLOBAL must be even.</span>
<span id="L158">NIGLOBAL = 4                    !</span>
<span id="L159">                                ! The total number of thickness grid points in the x-direction in the physical</span>
<span id="L160">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L161">NJGLOBAL = 4                    !</span>
<span id="L162">                                ! The total number of thickness grid points in the y-direction in the physical</span>
<span id="L163">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L164">NIHALO = 4                      ! default = 4</span>
<span id="L165">                                ! The number of halo points on each side in the x-direction.  How this is set</span>
<span id="L166">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L167">NJHALO = 4                      ! default = 4</span>
<span id="L168">                                ! The number of halo points on each side in the y-direction.  How this is set</span>
<span id="L169">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L170"></span>
<span id="L171">! === module MOM_hor_index ===</span>
<span id="L172">! Sets the horizontal array index types.</span>
<span id="L173"></span>
<span id="L174">! === module MOM_grid ===</span>
<span id="L175">! Parameters providing information about the lateral grid.</span>
<span id="L176">REFERENCE_HEIGHT = 0.0          !   [m] default = 0.0</span>
<span id="L177">                                ! A reference value for geometric height fields, such as bathyT.</span>
<span id="L178"></span>
<span id="L179">! === module MOM_fixed_initialization ===</span>
<span id="L180">INPUTDIR = &quot;.&quot;                  ! default = &quot;.&quot;</span>
<span id="L181">                                ! The directory in which input files are found.</span>
<span id="L182"></span>
<span id="L183">! === module MOM_grid_init ===</span>
<span id="L184">GRID_CONFIG = &quot;cartesian&quot;       !</span>
<span id="L185">                                ! A character string that determines the method for defining the horizontal</span>
<span id="L186">                                ! grid.  Current options are:</span>
<span id="L187">                                !     mosaic - read the grid from a mosaic (supergrid)</span>
<span id="L188">                                !              file set by GRID_FILE.</span>
<span id="L189">                                !     cartesian - use a (flat) Cartesian grid.</span>
<span id="L190">                                !     spherical - use a simple spherical grid.</span>
<span id="L191">                                !     mercator - use a Mercator spherical grid.</span>
<span id="L192">AXIS_UNITS = &quot;degrees&quot;          ! default = &quot;degrees&quot;</span>
<span id="L193">                                ! The units for the Cartesian axes. Valid entries are:</span>
<span id="L194">                                !     degrees - degrees of latitude and longitude</span>
<span id="L195">                                !     m or meter(s) - meters</span>
<span id="L196">                                !     k or km or kilometer(s) - kilometers</span>
<span id="L197">SOUTHLAT = 0.0                  !   [degrees]</span>
<span id="L198">                                ! The southern latitude of the domain or the equivalent starting value for the</span>
<span id="L199">                                ! y-axis.</span>
<span id="L200">LENLAT = 1.0                    !   [degrees]</span>
<span id="L201">                                ! The latitudinal or y-direction length of the domain.</span>
<span id="L202">WESTLON = 0.0                   !   [degrees] default = 0.0</span>
<span id="L203">                                ! The western longitude of the domain or the equivalent starting value for the</span>
<span id="L204">                                ! x-axis.</span>
<span id="L205">LENLON = 1.0                    !   [degrees]</span>
<span id="L206">                                ! The longitudinal or x-direction length of the domain.</span>
<span id="L207">RAD_EARTH = 6.378E+06           !   [m] default = 6.378E+06</span>
<span id="L208">                                ! The radius of the Earth.</span>
<span id="L209">TOPO_CONFIG = &quot;flat&quot;            !</span>
<span id="L210">                                ! This specifies how bathymetry is specified:</span>
<span id="L211">                                !     file - read bathymetric information from the file</span>
<span id="L212">                                !       specified by (TOPO_FILE).</span>
<span id="L213">                                !     flat - flat bottom set to MAXIMUM_DEPTH.</span>
<span id="L214">                                !     bowl - an analytically specified bowl-shaped basin</span>
<span id="L215">                                !       ranging between MAXIMUM_DEPTH and MINIMUM_DEPTH.</span>
<span id="L216">                                !     spoon - a similar shape to &#x27;bowl&#x27;, but with an vertical</span>
<span id="L217">                                !       wall at the southern face.</span>
<span id="L218">                                !     halfpipe - a zonally uniform channel with a half-sine</span>
<span id="L219">                                !       profile in the meridional direction.</span>
<span id="L220">                                !     bbuilder - build topography from list of functions.</span>
<span id="L221">                                !     benchmark - use the benchmark test case topography.</span>
<span id="L222">                                !     Neverworld - use the Neverworld test case topography.</span>
<span id="L223">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L224">                                !       DOME sill-overflow test case.</span>
<span id="L225">                                !     ISOMIP - use a slope and channel configuration for the</span>
<span id="L226">                                !       ISOMIP test case.</span>
<span id="L227">                                !     DOME2D - use a shelf and slope configuration for the</span>
<span id="L228">                                !       DOME2D gravity current/overflow test case.</span>
<span id="L229">                                !     Kelvin - flat but with rotated land mask.</span>
<span id="L230">                                !     seamount - Gaussian bump for spontaneous motion test case.</span>
<span id="L231">                                !     dumbbell - Sloshing channel with reservoirs on both ends.</span>
<span id="L232">                                !     shelfwave - exponential slope for shelfwave test case.</span>
<span id="L233">                                !     Phillips - ACC-like idealized topography used in the Phillips config.</span>
<span id="L234">                                !     dense - Denmark Strait-like dense water formation and overflow.</span>
<span id="L235">                                !     USER - call a user modified routine.</span>
<span id="L236">MINIMUM_DEPTH = 0.0             !   [m] default = 0.0</span>
<span id="L237">                                ! The minimum depth of the ocean.</span>
<span id="L238">MAXIMUM_DEPTH = 100.0           !   [m]</span>
<span id="L239">                                ! The maximum depth of the ocean.</span>
<span id="L240"></span>
<span id="L241">! === module MOM_open_boundary ===</span>
<span id="L242">! Controls where open boundaries are located, what kind of boundary condition to impose, and what data to apply,</span>
<span id="L243">! if any.</span>
<span id="L244">OBC_NUMBER_OF_SEGMENTS = 0      ! default = 0</span>
<span id="L245">                                ! The number of open boundary segments.</span>
<span id="L246">MASKING_DEPTH = -9999.0         !   [m] default = -9999.0</span>
<span id="L247">                                ! The depth below which to mask points as land points, for which all fluxes are</span>
<span id="L248">                                ! zeroed out. MASKING_DEPTH is ignored if it has the special default value.</span>
<span id="L249">CHANNEL_CONFIG = &quot;none&quot;         ! default = &quot;none&quot;</span>
<span id="L250">                                ! A parameter that determines which set of channels are</span>
<span id="L251">                                ! restricted to specific  widths.  Options are:</span>
<span id="L252">                                !     none - All channels have the grid width.</span>
<span id="L253">                                !     global_1deg - Sets 16 specific channels appropriate</span>
<span id="L254">                                !       for a 1-degree model, as used in CM2G.</span>
<span id="L255">                                !     list - Read the channel locations and widths from a</span>
<span id="L256">                                !       text file, like MOM_channel_list in the MOM_SIS</span>
<span id="L257">                                !       test case.</span>
<span id="L258">                                !     file - Read open face widths everywhere from a</span>
<span id="L259">                                !       NetCDF file on the model grid.</span>
<span id="L260">SUBGRID_TOPO_AT_VEL = False     !   [Boolean] default = False</span>
<span id="L261">                                ! If true, use variables from TOPO_AT_VEL_FILE as parameters for porous barrier.</span>
<span id="L262">ROTATION = &quot;2omegasinlat&quot;       ! default = &quot;2omegasinlat&quot;</span>
<span id="L263">                                ! This specifies how the Coriolis parameter is specified:</span>
<span id="L264">                                !     2omegasinlat - Use twice the planetary rotation rate</span>
<span id="L265">                                !       times the sine of latitude.</span>
<span id="L266">                                !     betaplane - Use a beta-plane or f-plane.</span>
<span id="L267">                                !     USER - call a user modified routine.</span>
<span id="L268">OMEGA = 7.2921E-05              !   [s-1] default = 7.2921E-05</span>
<span id="L269">                                ! The rotation rate of the earth.</span>
<span id="L270">GRID_ROTATION_ANGLE_BUGS = False !   [Boolean] default = False</span>
<span id="L271">                                ! If true, use an older algorithm to calculate the sine and cosines needed</span>
<span id="L272">                                ! rotate between grid-oriented directions and true north and east.  Differences</span>
<span id="L273">                                ! arise at the tripolar fold.</span>
<span id="L274"></span>
<span id="L275">! === module MOM_verticalGrid ===</span>
<span id="L276">! Parameters providing information about the vertical grid.</span>
<span id="L277">G_EARTH = 9.8                   !   [m s-2] default = 9.8</span>
<span id="L278">                                ! The gravitational acceleration of the Earth.</span>
<span id="L279">RHO_0 = 1035.0                  !   [kg m-3] default = 1035.0</span>
<span id="L280">                                ! The mean ocean density used with BOUSSINESQ true to calculate accelerations</span>
<span id="L281">                                ! and the mass for conservation properties, or with BOUSSINSEQ false to convert</span>
<span id="L282">                                ! some parameters from vertical units of m to kg m-2.</span>
<span id="L283">BOUSSINESQ = True               !   [Boolean] default = True</span>
<span id="L284">                                ! If true, make the Boussinesq approximation.</span>
<span id="L285">ANGSTROM = 1.0E-10              !   [m] default = 1.0E-10</span>
<span id="L286">                                ! The minimum layer thickness, usually one-Angstrom.</span>
<span id="L287">H_TO_M = 1.0                    !   [m H-1] default = 1.0</span>
<span id="L288">                                ! A constant that translates the model&#x27;s internal units of thickness into m.</span>
<span id="L289">NK = 1                          !   [nondim]</span>
<span id="L290">                                ! The number of model layers.</span>
<span id="L291">ADVECTION_SCHEME_VARIANCE_UNDERFLOW = 1.0E-23 !   [Conc2 (tracer dependent)] default = 1.0E-23</span>
<span id="L292">                                ! A tiny magnitude for variance used to determine when advection scheme variance</span>
<span id="L293">                                ! production is set to 0.</span>
<span id="L294"></span>
<span id="L295">! === module MOM_tracer_registry ===</span>
<span id="L296"></span>
<span id="L297">! === module MOM_restart ===</span>
<span id="L298">PARALLEL_RESTARTFILES = False   !   [Boolean] default = False</span>
<span id="L299">                                ! If true, the IO layout is used to group processors that write to the same</span>
<span id="L300">                                ! restart file or each processor writes its own (numbered) restart file. If</span>
<span id="L301">                                ! false, a single restart file is generated combining output from all PEs.</span>
<span id="L302">RESTARTFILE = &quot;MOM.res&quot;         ! default = &quot;MOM.res&quot;</span>
<span id="L303">                                ! The name-root of the restart file.</span>
<span id="L304">MAX_FIELDS = 100                ! default = 100</span>
<span id="L305">                                ! The maximum number of restart fields that can be used.</span>
<span id="L306">RESTART_CHECKSUMS_REQUIRED = True !   [Boolean] default = True</span>
<span id="L307">                                ! If true, require the restart checksums to match and error out otherwise. Users</span>
<span id="L308">                                ! may want to avoid this comparison if for example the restarts are made from a</span>
<span id="L309">                                ! run with a different mask_table than the current run, in which case the</span>
<span id="L310">                                ! checksums will not match and cause crash.</span>
<span id="L311">RESTART_SYMMETRIC_CHECKSUMS = False !   [Boolean] default = False</span>
<span id="L312">                                ! If true, do the restart checksums on all the edge points for a non-reentrant</span>
<span id="L313">                                ! grid.  This requires that SYMMETRIC_MEMORY_ is defined at compile time.</span>
<span id="L314">RESTART_UNSIGNED_ZEROS = False  !   [Boolean] default = False</span>
<span id="L315">                                ! If true, convert any negative zeros that would be written to the restart file</span>
<span id="L316">                                ! into ordinary unsigned zeros.  This does not change answers, but it can be</span>
<span id="L317">                                ! helpful in comparing restart files after grid rotation, for example.</span>
<span id="L318"></span>
<span id="L319">! === module MOM_tracer_flow_control ===</span>
<span id="L320">USE_USER_TRACER_EXAMPLE = False !   [Boolean] default = False</span>
<span id="L321">                                ! If true, use the USER_tracer_example tracer package.</span>
<span id="L322">USE_DOME_TRACER = False         !   [Boolean] default = False</span>
<span id="L323">                                ! If true, use the DOME_tracer tracer package.</span>
<span id="L324">USE_ISOMIP_TRACER = False       !   [Boolean] default = False</span>
<span id="L325">                                ! If true, use the ISOMIP_tracer tracer package.</span>
<span id="L326">USE_RGC_TRACER = False          !   [Boolean] default = False</span>
<span id="L327">                                ! If true, use the RGC_tracer tracer package.</span>
<span id="L328">USE_IDEAL_AGE_TRACER = False    !   [Boolean] default = False</span>
<span id="L329">                                ! If true, use the ideal_age_example tracer package.</span>
<span id="L330">USE_MARBL_TRACERS = False       !   [Boolean] default = False</span>
<span id="L331">                                ! If true, use the MARBL tracer package.</span>
<span id="L332">USE_REGIONAL_DYES = False       !   [Boolean] default = False</span>
<span id="L333">                                ! If true, use the regional_dyes tracer package.</span>
<span id="L334">USE_FILE_DYES = False           !   [Boolean] default = False</span>
<span id="L335">                                ! If true, use the file dyes tracer package.</span>
<span id="L336">USE_OIL_TRACER = False          !   [Boolean] default = False</span>
<span id="L337">                                ! If true, use the oil_tracer tracer package.</span>
<span id="L338">USE_ADVECTION_TEST_TRACER = False !   [Boolean] default = False</span>
<span id="L339">                                ! If true, use the advection_test_tracer tracer package.</span>
<span id="L340">USE_OCMIP2_CFC = False          !   [Boolean] default = False</span>
<span id="L341">                                ! If true, use the MOM_OCMIP2_CFC tracer package.</span>
<span id="L342">USE_CFC_CAP = False             !   [Boolean] default = False</span>
<span id="L343">                                ! If true, use the MOM_CFC_cap tracer package.</span>
<span id="L344">USE_generic_tracer = False      !   [Boolean] default = False</span>
<span id="L345">                                ! If true and _USE_GENERIC_TRACER is defined as a preprocessor macro, use the</span>
<span id="L346">                                ! MOM_generic_tracer packages.</span>
<span id="L347">USE_PSEUDO_SALT_TRACER = False  !   [Boolean] default = False</span>
<span id="L348">                                ! If true, use the pseudo salt tracer, typically run as a diagnostic.</span>
<span id="L349">USE_BOUNDARY_IMPULSE_TRACER = False !   [Boolean] default = False</span>
<span id="L350">                                ! If true, use the boundary impulse tracer.</span>
<span id="L351">USE_DYED_OBC_TRACER = False     !   [Boolean] default = False</span>
<span id="L352">                                ! If true, use the dyed_obc_tracer tracer package.</span>
<span id="L353">USE_NW2_TRACERS = False         !   [Boolean] default = False</span>
<span id="L354">                                ! If true, use the NeverWorld2 tracers.</span>
<span id="L355"></span>
<span id="L356">! === module MOM_coord_initialization ===</span>
<span id="L357">COORD_CONFIG = &quot;none&quot;           ! default = &quot;none&quot;</span>
<span id="L358">                                ! This specifies how layers are to be defined:</span>
<span id="L359">                                !     ALE or none - used to avoid defining layers in ALE mode</span>
<span id="L360">                                !     file - read coordinate information from the file</span>
<span id="L361">                                !       specified by (COORD_FILE).</span>
<span id="L362">                                !     BFB - Custom coords for buoyancy-forced basin case</span>
<span id="L363">                                !       based on SST_S, T_BOT and DRHO_DT.</span>
<span id="L364">                                !     linear - linear based on interfaces not layers</span>
<span id="L365">                                !     layer_ref - linear based on layer densities</span>
<span id="L366">                                !     ts_ref - use reference temperature and salinity</span>
<span id="L367">                                !     ts_range - use range of temperature and salinity</span>
<span id="L368">                                !       (T_REF and S_REF) to determine surface density</span>
<span id="L369">                                !       and GINT calculate internal densities.</span>
<span id="L370">                                !     gprime - use reference density (RHO_0) for surface</span>
<span id="L371">                                !       density and GINT calculate internal densities.</span>
<span id="L372">                                !     ts_profile - use temperature and salinity profiles</span>
<span id="L373">                                !       (read from COORD_FILE) to set layer densities.</span>
<span id="L374">                                !     USER - call a user modified routine.</span>
<span id="L375">GFS = 9.8                       !   [m s-2] default = 9.8</span>
<span id="L376">                                ! The reduced gravity at the free surface.</span>
<span id="L377">LIGHTEST_DENSITY = 1035.0       !   [kg m-3] default = 1035.0</span>
<span id="L378">                                ! The reference potential density used for layer 1.</span>
<span id="L379"></span>
<span id="L380">! === module MOM_state_initialization ===</span>
<span id="L381">FATAL_INCONSISTENT_RESTART_TIME = False !   [Boolean] default = False</span>
<span id="L382">                                ! If true and a time_in value is provided to MOM_initialize_state, verify that</span>
<span id="L383">                                ! the time read from a restart file is the same as time_in, and issue a fatal</span>
<span id="L384">                                ! error if it is not.  Otherwise, simply set the time to time_in if present.</span>
<span id="L385">INIT_LAYERS_FROM_Z_FILE = False !   [Boolean] default = False</span>
<span id="L386">                                ! If true, initialize the layer thicknesses, temperatures, and salinities from a</span>
<span id="L387">                                ! Z-space file on a latitude-longitude grid.</span>
<span id="L388">THICKNESS_CONFIG = &quot;uniform&quot;    ! default = &quot;uniform&quot;</span>
<span id="L389">                                ! A string that determines how the initial layer thicknesses are specified for a</span>
<span id="L390">                                ! new run:</span>
<span id="L391">                                !     file - read interface heights from the file specified</span>
<span id="L392">                                !       by (THICKNESS_FILE).</span>
<span id="L393">                                !     thickness_file - read thicknesses from the file specified</span>
<span id="L394">                                !       by (THICKNESS_FILE).</span>
<span id="L395">                                !     mass_file - read thicknesses in units of mass per unit area from the file</span>
<span id="L396">                                !       specified by (THICKNESS_FILE).</span>
<span id="L397">                                !     coord - determined by ALE coordinate.</span>
<span id="L398">                                !     uniform - uniform thickness layers evenly distributed</span>
<span id="L399">                                !       between the surface and MAXIMUM_DEPTH.</span>
<span id="L400">                                !     list - read a list of positive interface depths.</span>
<span id="L401">                                !     param - use thicknesses from parameter THICKNESS_INIT_VALUES.</span>
<span id="L402">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L403">                                !       DOME sill-overflow test case.</span>
<span id="L404">                                !     ISOMIP - use a configuration for the</span>
<span id="L405">                                !       ISOMIP test case.</span>
<span id="L406">                                !     benchmark - use the benchmark test case thicknesses.</span>
<span id="L407">                                !     Neverworld - use the Neverworld test case thicknesses.</span>
<span id="L408">                                !     search - search a density profile for the interface</span>
<span id="L409">                                !       densities. This is not yet implemented.</span>
<span id="L410">                                !     circle_obcs - the circle_obcs test case is used.</span>
<span id="L411">                                !     DOME2D - 2D version of DOME initialization.</span>
<span id="L412">                                !     adjustment2d - 2D lock exchange thickness ICs.</span>
<span id="L413">                                !     sloshing - sloshing gravity thickness ICs.</span>
<span id="L414">                                !     seamount - no motion test with seamount ICs.</span>
<span id="L415">                                !     dumbbell - sloshing channel ICs.</span>
<span id="L416">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L417">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L418">                                !     USER - call a user modified routine.</span>
<span id="L419">DEPRESS_INITIAL_SURFACE = False !   [Boolean] default = False</span>
<span id="L420">                                ! If true,  depress the initial surface to avoid huge tsunamis when a large</span>
<span id="L421">                                ! surface pressure is applied.</span>
<span id="L422">TRIM_IC_FOR_P_SURF = False      !   [Boolean] default = False</span>
<span id="L423">                                ! If true, cuts way the top of the column for initial conditions at the depth</span>
<span id="L424">                                ! where the hydrostatic pressure matches the imposed surface pressure which is</span>
<span id="L425">                                ! read from file.</span>
<span id="L426">VELOCITY_CONFIG = &quot;zero&quot;        ! default = &quot;zero&quot;</span>
<span id="L427">                                ! A string that determines how the initial velocities are specified for a new</span>
<span id="L428">                                ! run:</span>
<span id="L429">                                !     file - read velocities from the file specified</span>
<span id="L430">                                !       by (VELOCITY_FILE).</span>
<span id="L431">                                !     zero - the fluid is initially at rest.</span>
<span id="L432">                                !     uniform - the flow is uniform (determined by</span>
<span id="L433">                                !       parameters INITIAL_U_CONST and INITIAL_V_CONST).</span>
<span id="L434">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L435">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L436">                                !     USER - call a user modified routine.</span>
<span id="L437">ODA_INCUPD = False              !   [Boolean] default = False</span>
<span id="L438">                                ! If true, oda incremental updates will be applied everywhere in the domain.</span>
<span id="L439">SPONGE = False                  !   [Boolean] default = False</span>
<span id="L440">                                ! If true, sponges may be applied anywhere in the domain. The exact location and</span>
<span id="L441">                                ! properties of those sponges are specified via SPONGE_CONFIG.</span>
<span id="L442"></span>
<span id="L443">! === module MOM_diag_mediator ===</span>
<span id="L444">NUM_DIAG_COORDS = 1             ! default = 1</span>
<span id="L445">                                ! The number of diagnostic vertical coordinates to use. For each coordinate, an</span>
<span id="L446">                                ! entry in DIAG_COORDS must be provided.</span>
<span id="L447">DIAG_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L448">                                ! If true, use the OM4 remapping-via-subcells algorithm for diagnostics. See</span>
<span id="L449">                                ! REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting this option to</span>
<span id="L450">                                ! false.</span>
<span id="L451">REMAPPING_ANSWER_DATE = 20181231 ! default = 20181231</span>
<span id="L452">                                ! The vintage of the expressions and order of arithmetic to use for remapping.</span>
<span id="L453">                                ! Values below 20190101 result in the use of older, less accurate expressions</span>
<span id="L454">                                ! that were in use at the end of 2018.  Higher values result in the use of more</span>
<span id="L455">                                ! robust and accurate forms of mathematically equivalent expressions.</span>
<span id="L456">USE_INDEX_DIAGNOSTIC_AXES = False !   [Boolean] default = False</span>
<span id="L457">                                ! If true, use a grid index coordinate convention for diagnostic axes.</span>
<span id="L458">DIAG_COORDS = &quot;z Z ZSTAR&quot;       ! default = &quot;z Z ZSTAR&quot;</span>
<span id="L459">                                ! A list of string tuples associating diag_table modules to a coordinate</span>
<span id="L460">                                ! definition used for diagnostics. Each string is of the form &quot;MODULE_SUFFIX</span>
<span id="L461">                                ! PARAMETER_SUFFIX COORDINATE_NAME&quot;.</span>
<span id="L462">DIAG_MISVAL = 1.0E+20           !   [various] default = 1.0E+20</span>
<span id="L463">                                ! Set the default missing value to use for diagnostics.</span>
<span id="L464">DIAG_AS_CHKSUM = False          !   [Boolean] default = False</span>
<span id="L465">                                ! Instead of writing diagnostics to the diag manager, write a text file</span>
<span id="L466">                                ! containing the checksum (bitcount) of the array.</span>
<span id="L467">AVAILABLE_DIAGS_FILE = &quot;available_diags.000000&quot; ! default = &quot;available_diags.000000&quot;</span>
<span id="L468">                                ! A file into which to write a list of all available ocean diagnostics that can</span>
<span id="L469">                                ! be included in a diag_table.</span>
<span id="L470">DIAG_COORD_DEF_Z = &quot;UNIFORM&quot;    ! default = &quot;UNIFORM&quot;</span>
<span id="L471">                                ! Determines how to specify the coordinate resolution. Valid options are:</span>
<span id="L472">                                !  PARAM       - use the vector-parameter DIAG_COORD_RES_Z</span>
<span id="L473">                                !  UNIFORM[:N] - uniformly distributed</span>
<span id="L474">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L475">                                !                the filename and variable name, separated</span>
<span id="L476">                                !                by a comma or space, e.g. FILE:lev.nc,dz</span>
<span id="L477">                                !                or FILE:lev.nc,interfaces=zw</span>
<span id="L478">                                !  WOA09[:N]   - the WOA09 vertical grid (approximately)</span>
<span id="L479">                                !  WOA09INT[:N] - layers spanned by the WOA09 depths</span>
<span id="L480">                                !  WOA23INT[:N] - layers spanned by the WOA23 depths</span>
<span id="L481">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L482">                                !  HYBRID:string - read from a file. The string specifies</span>
<span id="L483">                                !                the filename and two variable names, separated</span>
<span id="L484">                                !                by a comma or space, for sigma-2 and dz.</span>
<span id="L485">                                !                e.g. HYBRID:vgrid.nc,sigma2,dz</span>
<span id="L486">                                !  HYBRID_3D:string - read from a file. The string specifies</span>
<span id="L487">                                !                the filename and two 3D variable names, separated</span>
<span id="L488">                                !                by a comma or space, for sigma-2 and dz. The</span>
<span id="L489">                                !                latter can be FNC1:string which is used everywhere.</span>
<span id="L490">                                !                e.g. HYBRID_3D:vgrid.nc,sigma2,dz</span>
<span id="L491">                                !  HYBRID_MAP:string - read from a file. The string specifies</span>
<span id="L492">                                !                the filename and three variable names, separated</span>
<span id="L493">                                !                by a comma or space, for map, sigma-2 and dz.</span>
<span id="L494">                                !                Map is a spatial index array with, maxval(map)=N,</span>
<span id="L495">                                !                and the others are 2D arrays containing N profiles.</span>
<span id="L496">                                !                Map typically contains integer values, but it can</span>
<span id="L497">                                !                contain real values, I+w, which imply using</span>
<span id="L498">                                !                the weighted sum of profiles I and I+1.</span>
<span id="L499">                                !                Dz can be FNC1:string which is used everywhere.</span>
<span id="L500">                                !                e.g. HYBRID_MAP:vgrid.nc,map,sigma2,dz</span>
<span id="L501"></span>
<span id="L502">! === module MOM_MEKE ===</span>
<span id="L503">USE_MEKE = False                !   [Boolean] default = False</span>
<span id="L504">                                ! If true, turns on the MEKE scheme which calculates a sub-grid mesoscale eddy</span>
<span id="L505">                                ! kinetic energy budget.</span>
<span id="L506"></span>
<span id="L507">! === module MOM_lateral_mixing_coeffs ===</span>
<span id="L508">USE_VARIABLE_MIXING = False     !   [Boolean] default = False</span>
<span id="L509">                                ! If true, the variable mixing code will be called.  This allows diagnostics to</span>
<span id="L510">                                ! be created even if the scheme is not used.  If KHTR_SLOPE_CFF&gt;0 or</span>
<span id="L511">                                ! KhTh_Slope_Cff&gt;0, this is set to true regardless of what is in the parameter</span>
<span id="L512">                                ! file.</span>
<span id="L513">USE_VISBECK = False             !   [Boolean] default = False</span>
<span id="L514">                                ! If true, use the Visbeck et al. (1997) formulation for</span>
<span id="L515">                                ! thickness diffusivity.</span>
<span id="L516">RESOLN_SCALED_KH = False        !   [Boolean] default = False</span>
<span id="L517">                                ! If true, the Laplacian lateral viscosity is scaled away when the first</span>
<span id="L518">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L519">DEPTH_SCALED_KHTH = False       !   [Boolean] default = False</span>
<span id="L520">                                ! If true, KHTH is scaled away when the depth is shallowerthan a reference</span>
<span id="L521">                                ! depth: KHTH = MIN(1,H/H0)**N * KHTH, where H0 is a reference depth, controlled</span>
<span id="L522">                                ! via DEPTH_SCALED_KHTH_H0, and the exponent (N) is controlled via</span>
<span id="L523">                                ! DEPTH_SCALED_KHTH_EXP.</span>
<span id="L524">RESOLN_SCALED_KHTH = False      !   [Boolean] default = False</span>
<span id="L525">                                ! If true, the interface depth diffusivity is scaled away when the first</span>
<span id="L526">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L527">RESOLN_SCALED_KHTR = False      !   [Boolean] default = False</span>
<span id="L528">                                ! If true, the epipycnal tracer diffusivity is scaled away when the first</span>
<span id="L529">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L530">RESOLN_USE_EBT = False          !   [Boolean] default = False</span>
<span id="L531">                                ! If true, uses the equivalent barotropic wave speed instead of first baroclinic</span>
<span id="L532">                                ! wave for calculating the resolution fn.</span>
<span id="L533">BACKSCAT_EBT_POWER = 0.0        !   [nondim] default = 0.0</span>
<span id="L534">                                ! Power to raise EBT vertical structure to when backscatter has vertical</span>
<span id="L535">                                ! structure.</span>
<span id="L536">BS_USE_SQG_STRUCT = False       !   [Boolean] default = False</span>
<span id="L537">                                ! If true, the SQG vertical structure is used for backscatter on the condition</span>
<span id="L538">                                ! that BS_EBT_power=0</span>
<span id="L539">KHTH_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L540">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L541">                                ! thickness diffusivity.</span>
<span id="L542">KHTH_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L543">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L544">                                ! of thickness diffusivity.</span>
<span id="L545">KHTR_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L546">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L547">                                ! tracer diffusivity.</span>
<span id="L548">KHTR_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L549">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L550">                                ! of tracer diffusivity.</span>
<span id="L551">KD_GL90_USE_EBT_STRUCT = False  !   [Boolean] default = False</span>
<span id="L552">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L553">                                ! diffusivity in the GL90 scheme.</span>
<span id="L554">KD_GL90_USE_SQG_STRUCT = False  !   [Boolean] default = False</span>
<span id="L555">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L556">                                ! diffusivity in the GL90 scheme.</span>
<span id="L557">KHTH_SLOPE_CFF = 0.0            !   [nondim] default = 0.0</span>
<span id="L558">                                ! The nondimensional coefficient in the Visbeck formula for the interface depth</span>
<span id="L559">                                ! diffusivity</span>
<span id="L560">KHTR_SLOPE_CFF = 0.0            !   [nondim] default = 0.0</span>
<span id="L561">                                ! The nondimensional coefficient in the Visbeck formula for the epipycnal tracer</span>
<span id="L562">                                ! diffusivity</span>
<span id="L563">USE_STORED_SLOPES = False       !   [Boolean] default = False</span>
<span id="L564">                                ! If true, the isopycnal slopes are calculated once and stored for re-use. This</span>
<span id="L565">                                ! uses more memory but avoids calling the equation of state more times than</span>
<span id="L566">                                ! should be necessary.</span>
<span id="L567">VERY_SMALL_FREQUENCY = 1.0E-17  !   [s-1] default = 1.0E-17</span>
<span id="L568">                                ! A miniscule frequency that is used to avoid division by 0.  The default value</span>
<span id="L569">                                ! is roughly (pi / (the age of the universe)).</span>
<span id="L570">USE_STANLEY_ISO = False         !   [Boolean] default = False</span>
<span id="L571">                                ! If true, turn on Stanley SGS T variance parameterization in isopycnal slope</span>
<span id="L572">                                ! code.</span>
<span id="L573">KD_SMOOTH = 1.0E-06             !   [m2 s-1] default = 1.0E-06</span>
<span id="L574">                                ! A diapycnal diffusivity that is used to interpolate more sensible values of T</span>
<span id="L575">                                ! &amp; S into thin layers.</span>
<span id="L576">USE_QG_LEITH_GM = False         !   [Boolean] default = False</span>
<span id="L577">                                ! If true, use the QG Leith viscosity as the GM coefficient.</span>
<span id="L578"></span>
<span id="L579">! === module MOM_set_visc ===</span>
<span id="L580">SET_VISC_ANSWER_DATE = 20181231 ! default = 20181231</span>
<span id="L581">                                ! The vintage of the order of arithmetic and expressions in the set viscosity</span>
<span id="L582">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L583">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L584">BOTTOMDRAGLAW = False           !   [Boolean] default = True</span>
<span id="L585">                                ! If true, the bottom stress is calculated with a drag law of the form</span>
<span id="L586">                                ! c_drag*|u|*u. The velocity magnitude may be an assumed value or it may be</span>
<span id="L587">                                ! based on the actual velocity in the bottommost HBBL, depending on LINEAR_DRAG.</span>
<span id="L588">CHANNEL_DRAG = False            !   [Boolean] default = False</span>
<span id="L589">                                ! If true, the bottom drag is exerted directly on each layer proportional to the</span>
<span id="L590">                                ! fraction of the bottom it overlies.</span>
<span id="L591">LINEAR_DRAG = False             !   [Boolean] default = False</span>
<span id="L592">                                ! If LINEAR_DRAG and BOTTOMDRAGLAW are defined the drag law is</span>
<span id="L593">                                ! cdrag*DRAG_BG_VEL*u.</span>
<span id="L594">DYNAMIC_VISCOUS_ML = False      !   [Boolean] default = False</span>
<span id="L595">                                ! If true, use a bulk Richardson number criterion to determine the mixed layer</span>
<span id="L596">                                ! thickness for viscosity.</span>
<span id="L597">HBBL = 1.0                      !   [m]</span>
<span id="L598">                                ! The thickness of a bottom boundary layer with a viscosity increased by</span>
<span id="L599">                                ! KV_EXTRA_BBL if BOTTOMDRAGLAW is not defined, or the thickness over which</span>
<span id="L600">                                ! near-bottom velocities are averaged for the drag law if BOTTOMDRAGLAW is</span>
<span id="L601">                                ! defined but LINEAR_DRAG is not.</span>
<span id="L602">BBL_THICK_MIN = 0.0             !   [m] default = 0.0</span>
<span id="L603">                                ! The minimum bottom boundary layer thickness that can be used with</span>
<span id="L604">                                ! BOTTOMDRAGLAW. This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum</span>
<span id="L605">                                ! near-bottom viscosity.</span>
<span id="L606">HTBL_SHELF_MIN = 0.0            !   [m] default = 0.0</span>
<span id="L607">                                ! The minimum top boundary layer thickness that can be used with BOTTOMDRAGLAW.</span>
<span id="L608">                                ! This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum near-top</span>
<span id="L609">                                ! viscosity.</span>
<span id="L610">HTBL_SHELF = 1.0                !   [m] default = 1.0</span>
<span id="L611">                                ! The thickness over which near-surface velocities are averaged for the drag law</span>
<span id="L612">                                ! under an ice shelf.  By default this is the same as HBBL</span>
<span id="L613">KV = 1.0                        !   [m2 s-1]</span>
<span id="L614">                                ! The background kinematic viscosity in the interior. The molecular value, ~1e-6</span>
<span id="L615">                                ! m2 s-1, may be used.</span>
<span id="L616">KV_BBL_MIN = 1.0                !   [m2 s-1] default = 1.0</span>
<span id="L617">                                ! The minimum viscosities in the bottom boundary layer.</span>
<span id="L618">KV_TBL_MIN = 1.0                !   [m2 s-1] default = 1.0</span>
<span id="L619">                                ! The minimum viscosities in the top boundary layer.</span>
<span id="L620">CORRECT_BBL_BOUNDS = False      !   [Boolean] default = False</span>
<span id="L621">                                ! If true, uses the correct bounds on the BBL thickness and viscosity so that</span>
<span id="L622">                                ! the bottom layer feels the intended drag.</span>
<span id="L623"></span>
<span id="L624">! === module MOM_thickness_diffuse ===</span>
<span id="L625">KHTH = 0.0                      !   [m2 s-1] default = 0.0</span>
<span id="L626">                                ! The background horizontal thickness diffusivity.</span>
<span id="L627">READ_KHTH = False               !   [Boolean] default = False</span>
<span id="L628">                                ! If true, read a file (given by KHTH_FILE) containing the spatially varying</span>
<span id="L629">                                ! horizontal isopycnal height diffusivity.</span>
<span id="L630">KHTH_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L631">                                ! The minimum horizontal thickness diffusivity.</span>
<span id="L632">KHTH_MAX = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L633">                                ! The maximum horizontal thickness diffusivity.</span>
<span id="L634">KHTH_MAX_CFL = 0.8              !   [nondimensional] default = 0.8</span>
<span id="L635">                                ! The maximum value of the local diffusive CFL ratio that is permitted for the</span>
<span id="L636">                                ! thickness diffusivity. 1.0 is the marginally unstable value in a pure layered</span>
<span id="L637">                                ! model, but much smaller numbers (e.g. 0.1) seem to work better for ALE-based</span>
<span id="L638">                                ! models.</span>
<span id="L639">KH_ETA_CONST = 0.0              !   [m2 s-1] default = 0.0</span>
<span id="L640">                                ! The background horizontal diffusivity of the interface heights (without</span>
<span id="L641">                                ! considering the layer density structure).  If diffusive CFL limits are</span>
<span id="L642">                                ! encountered, the diffusivities of the isopycnals and the interfaces heights</span>
<span id="L643">                                ! are scaled back proportionately.</span>
<span id="L644">KH_ETA_VEL_SCALE = 0.0          !   [m s-1] default = 0.0</span>
<span id="L645">                                ! A velocity scale that is multiplied by the grid spacing to give a contribution</span>
<span id="L646">                                ! to the horizontal diffusivity of the interface heights (without considering</span>
<span id="L647">                                ! the layer density structure).</span>
<span id="L648">DETANGLE_INTERFACES = False     !   [Boolean] default = False</span>
<span id="L649">                                ! If defined add 3-d structured enhanced interface height diffusivities to</span>
<span id="L650">                                ! horizontally smooth jagged layers.</span>
<span id="L651">KHTH_SLOPE_MAX = 0.01           !   [nondim] default = 0.01</span>
<span id="L652">                                ! A slope beyond which the calculated isopycnal slope is not reliable and is</span>
<span id="L653">                                ! scaled away.</span>
<span id="L654">KHTH_USE_FGNV_STREAMFUNCTION = False !   [Boolean] default = False</span>
<span id="L655">                                ! If true, use the streamfunction formulation of Ferrari et al., 2010, which</span>
<span id="L656">                                ! effectively emphasizes graver vertical modes by smoothing in the vertical.</span>
<span id="L657">USE_STANLEY_GM = False          !   [Boolean] default = False</span>
<span id="L658">                                ! If true, turn on Stanley SGS T variance parameterization in GM code.</span>
<span id="L659">MEKE_GM_SRC_ALT = False         !   [Boolean] default = False</span>
<span id="L660">                                ! If true, use the GM energy conversion form S^2*N^2*kappa rather than the</span>
<span id="L661">                                ! streamfunction for the GM source term.</span>
<span id="L662">MEKE_GEOMETRIC = False          !   [Boolean] default = False</span>
<span id="L663">                                ! If true, uses the GM coefficient formulation from the GEOMETRIC framework</span>
<span id="L664">                                ! (Marshall et al., 2012).</span>
<span id="L665">USE_GME = False                 !   [Boolean] default = False</span>
<span id="L666">                                ! If true, use the GM+E backscatter scheme in association with the Gent and</span>
<span id="L667">                                ! McWilliams parameterization.</span>
<span id="L668">USE_GM_WORK_BUG = False         !   [Boolean] default = False</span>
<span id="L669">                                ! If true, compute the top-layer work tendency on the u-grid with the incorrect</span>
<span id="L670">                                ! sign, for legacy reproducibility.</span>
<span id="L671"></span>
<span id="L672">! === module MOM_dynamics_unsplit ===</span>
<span id="L673">UNSPLIT_DT_VISC_BUG = False     !   [Boolean] default = False</span>
<span id="L674">                                ! If false, use the correct timestep in the viscous terms applied in the first</span>
<span id="L675">                                ! predictor step with the unsplit time stepping scheme, and in the calculation</span>
<span id="L676">                                ! of the turbulent mixed layer properties for viscosity with unsplit or</span>
<span id="L677">                                ! unsplit_RK2.  If true, an older incorrect value is used.</span>
<span id="L678">TIDES = False                   !   [Boolean] default = False</span>
<span id="L679">                                ! If true, apply tidal momentum forcing.</span>
<span id="L680">CALCULATE_SAL = False           !   [Boolean] default = False</span>
<span id="L681">                                ! If true, calculate self-attraction and loading.</span>
<span id="L682"></span>
<span id="L683">! === module MOM_continuity_PPM ===</span>
<span id="L684">MONOTONIC_CONTINUITY = False    !   [Boolean] default = False</span>
<span id="L685">                                ! If true, CONTINUITY_PPM uses the Colella and Woodward monotonic limiter.  The</span>
<span id="L686">                                ! default (false) is to use a simple positive definite limiter.</span>
<span id="L687">SIMPLE_2ND_PPM_CONTINUITY = True !   [Boolean] default = False</span>
<span id="L688">                                ! If true, CONTINUITY_PPM uses a simple 2nd order (arithmetic mean)</span>
<span id="L689">                                ! interpolation of the edge values. This may give better PV conservation</span>
<span id="L690">                                ! properties. While it formally reduces the accuracy of the continuity solver</span>
<span id="L691">                                ! itself in the strongly advective limit, it does not reduce the overall order</span>
<span id="L692">                                ! of accuracy of the dynamic core.</span>
<span id="L693">UPWIND_1ST_CONTINUITY = False   !   [Boolean] default = False</span>
<span id="L694">                                ! If true, CONTINUITY_PPM becomes a 1st-order upwind continuity solver.  This</span>
<span id="L695">                                ! scheme is highly diffusive but may be useful for debugging or in single-column</span>
<span id="L696">                                ! mode where its minimal stencil is useful.</span>
<span id="L697">ETA_TOLERANCE = 5.0E-11         !   [m] default = 5.0E-11</span>
<span id="L698">                                ! The tolerance for the differences between the barotropic and baroclinic</span>
<span id="L699">                                ! estimates of the sea surface height due to the fluxes through each face.  The</span>
<span id="L700">                                ! total tolerance for SSH is 4 times this value.  The default is</span>
<span id="L701">                                ! 0.5*NK*ANGSTROM, and this should not be set less than about</span>
<span id="L702">                                ! 10^-15*MAXIMUM_DEPTH.</span>
<span id="L703">VELOCITY_TOLERANCE = 3.0E+08    !   [m s-1] default = 3.0E+08</span>
<span id="L704">                                ! The tolerance for barotropic velocity discrepancies between the barotropic</span>
<span id="L705">                                ! solution and  the sum of the layer thicknesses.</span>
<span id="L706">CONT_PPM_AGGRESS_ADJUST = False !   [Boolean] default = False</span>
<span id="L707">                                ! If true, allow the adjusted velocities to have a relative CFL change up to</span>
<span id="L708">                                ! 0.5.</span>
<span id="L709">CONT_PPM_VOLUME_BASED_CFL = False !   [Boolean] default = False</span>
<span id="L710">                                ! If true, use the ratio of the open face lengths to the tracer cell areas when</span>
<span id="L711">                                ! estimating CFL numbers.  The default is set by CONT_PPM_AGGRESS_ADJUST.</span>
<span id="L712">CONTINUITY_CFL_LIMIT = 0.5      !   [nondim] default = 0.5</span>
<span id="L713">                                ! The maximum CFL of the adjusted velocities.</span>
<span id="L714">CONT_PPM_BETTER_ITER = True     !   [Boolean] default = True</span>
<span id="L715">                                ! If true, stop corrective iterations using a velocity based criterion and only</span>
<span id="L716">                                ! stop if the iteration is better than all predecessors.</span>
<span id="L717">CONT_PPM_USE_VISC_REM_MAX = True !   [Boolean] default = True</span>
<span id="L718">                                ! If true, use more appropriate limiting bounds for corrections in strongly</span>
<span id="L719">                                ! viscous columns.</span>
<span id="L720">CONT_PPM_MARGINAL_FACE_AREAS = True !   [Boolean] default = True</span>
<span id="L721">                                ! If true, use the marginal face areas from the continuity solver for use as the</span>
<span id="L722">                                ! weights in the barotropic solver. Otherwise use the transport averaged areas.</span>
<span id="L723"></span>
<span id="L724">! === module MOM_CoriolisAdv ===</span>
<span id="L725">NOSLIP = False                  !   [Boolean] default = False</span>
<span id="L726">                                ! If true, no slip boundary conditions are used; otherwise free slip boundary</span>
<span id="L727">                                ! conditions are assumed. The implementation of the free slip BCs on a C-grid is</span>
<span id="L728">                                ! much cleaner than the no slip BCs. The use of free slip BCs is strongly</span>
<span id="L729">                                ! encouraged, and no slip BCs are not used with the biharmonic viscosity.</span>
<span id="L730">CORIOLIS_EN_DIS = False         !   [Boolean] default = False</span>
<span id="L731">                                ! If true, two estimates of the thickness fluxes are used to estimate the</span>
<span id="L732">                                ! Coriolis term, and the one that dissipates energy relative to the other one is</span>
<span id="L733">                                ! used.</span>
<span id="L734">CORIOLIS_SCHEME = &quot;SADOURNY75_ENERGY&quot; ! default = &quot;SADOURNY75_ENERGY&quot;</span>
<span id="L735">                                ! CORIOLIS_SCHEME selects the discretization for the Coriolis terms. Valid</span>
<span id="L736">                                ! values are:</span>
<span id="L737">                                !    SADOURNY75_ENERGY - Sadourny, 1975; energy cons.</span>
<span id="L738">                                !    ARAKAWA_HSU90     - Arakawa &amp; Hsu, 1990</span>
<span id="L739">                                !    SADOURNY75_ENSTRO - Sadourny, 1975; enstrophy cons.</span>
<span id="L740">                                !    ARAKAWA_LAMB81    - Arakawa &amp; Lamb, 1981; En. + Enst.</span>
<span id="L741">                                !    ARAKAWA_LAMB_BLEND - A blend of Arakawa &amp; Lamb with</span>
<span id="L742">                                !                         Arakawa &amp; Hsu and Sadourny energy</span>
<span id="L743">                                !    WENOVI5TH_PV_ENSTRO   - 5th-order WENO PV enstrophy</span>
<span id="L744">                                !    WENOVI3RD_PV_ENSTRO   - 3rd-order WENO PV enstrophy</span>
<span id="L745">                                !    WENOVI7TH_PV_ENSTRO  - 7th-order WENO PV enstrophy</span>
<span id="L746">BOUND_CORIOLIS = False          !   [Boolean] default = False</span>
<span id="L747">                                ! If true, the Coriolis terms at u-points are bounded by the four estimates of</span>
<span id="L748">                                ! (f+rv)v from the four neighboring v-points, and similarly at v-points.  This</span>
<span id="L749">                                ! option would have no effect on the SADOURNY Coriolis scheme if it were</span>
<span id="L750">                                ! possible to use centered difference thickness fluxes.</span>
<span id="L751">KE_SCHEME = &quot;KE_ARAKAWA&quot;        ! default = &quot;KE_ARAKAWA&quot;</span>
<span id="L752">                                ! KE_SCHEME selects the discretization for acceleration due to the kinetic</span>
<span id="L753">                                ! energy gradient. Valid values are:</span>
<span id="L754">                                !    KE_ARAKAWA, KE_SIMPLE_GUDONOV, KE_GUDONOV, KE_UP3</span>
<span id="L755">PV_ADV_SCHEME = &quot;PV_ADV_CENTERED&quot; ! default = &quot;PV_ADV_CENTERED&quot;</span>
<span id="L756">                                ! PV_ADV_SCHEME selects the discretization for PV advection. Valid values are:</span>
<span id="L757">                                !    PV_ADV_CENTERED - centered (aka Sadourny, 75)</span>
<span id="L758">                                !    PV_ADV_UPWIND1  - upwind, first order</span>
<span id="L759"></span>
<span id="L760">! === module MOM_PressureForce ===</span>
<span id="L761">ANALYTIC_FV_PGF = True          !   [Boolean] default = True</span>
<span id="L762">                                ! If true the pressure gradient forces are calculated with a finite volume form</span>
<span id="L763">                                ! that analytically integrates the equations of state in pressure to avoid any</span>
<span id="L764">                                ! possibility of numerical thermobaric instability, as described in Adcroft et</span>
<span id="L765">                                ! al., O. Mod. (2008).</span>
<span id="L766"></span>
<span id="L767">! === module MOM_PressureForce_FV ===</span>
<span id="L768">RHO_PGF_REF = 1035.0            !   [kg m-3] default = 1035.0</span>
<span id="L769">                                ! The reference density that is subtracted off when calculating pressure</span>
<span id="L770">                                ! gradient forces.  Its inverse is subtracted off of specific volumes when in</span>
<span id="L771">                                ! non-Boussinesq mode.  The default is RHO_0.</span>
<span id="L772">RHO_PGF_REF_BUG = True          !   [Boolean] default = True</span>
<span id="L773">                                ! If true, recover a bug that RHO_0 (the mean seawater density in Boussinesq</span>
<span id="L774">                                ! mode) and RHO_PGF_REF (the subtracted reference density in finite volume</span>
<span id="L775">                                ! pressure gradient forces) are incorrectly interchanged in several instances in</span>
<span id="L776">                                ! Boussinesq mode.</span>
<span id="L777">SSH_IN_EOS_PRESSURE_FOR_PGF = False !   [Boolean] default = False</span>
<span id="L778">                                ! If true, include contributions from the sea surface height in the height-based</span>
<span id="L779">                                ! pressure used in the equation of state calculations for the Boussinesq</span>
<span id="L780">                                ! pressure gradient forces, including adjustments for atmospheric or sea-ice</span>
<span id="L781">                                ! pressure.</span>
<span id="L782">MASS_WEIGHT_IN_PRESSURE_GRADIENT = False !   [Boolean] default = False</span>
<span id="L783">                                ! If true, use mass weighting when interpolating T/S for integrals near the</span>
<span id="L784">                                ! bathymetry in FV pressure gradient calculations.</span>
<span id="L785">MASS_WEIGHT_IN_PRESSURE_GRADIENT_TOP = False !   [Boolean] default = False</span>
<span id="L786">                                ! If true and MASS_WEIGHT_IN_PRESSURE_GRADIENT is true, use mass weighting when</span>
<span id="L787">                                ! interpolating T/S for integrals near the top of the water column in FV</span>
<span id="L788">                                ! pressure gradient calculations.</span>
<span id="L789">MASS_WEIGHT_IN_PGF_VANISHED_ONLY = False !   [Boolean] default = False</span>
<span id="L790">                                ! If true, use mass weighting when interpolating T/S for integrals only if one</span>
<span id="L791">                                ! side is vanished according to RESET_INTXPA_H_NONVANISHED.</span>
<span id="L792">USE_INACCURATE_PGF_RHO_ANOM = False !   [Boolean] default = False</span>
<span id="L793">                                ! If true, use a form of the PGF that uses the reference density in an</span>
<span id="L794">                                ! inaccurate way. This is not recommended.</span>
<span id="L795">RECONSTRUCT_FOR_PRESSURE = False !   [Boolean] default = False</span>
<span id="L796">                                ! If True, use vertical reconstruction of T &amp; S within the integrals of the FV</span>
<span id="L797">                                ! pressure gradient calculation. If False, use the constant-by-layer algorithm.</span>
<span id="L798">                                ! The default is set by USE_REGRIDDING.</span>
<span id="L799">PRESSURE_RECONSTRUCTION_SCHEME = 1 ! default = 1</span>
<span id="L800">                                ! Order of vertical reconstruction of T/S to use in the integrals within the FV</span>
<span id="L801">                                ! pressure gradient calculation.</span>
<span id="L802">                                !  0: PCM or no reconstruction.</span>
<span id="L803">                                !  1: PLM reconstruction.</span>
<span id="L804">                                !  2: PPM reconstruction.</span>
<span id="L805">BOUNDARY_EXTRAPOLATION_PRESSURE = True !   [Boolean] default = True</span>
<span id="L806">                                ! If true, the reconstruction of T &amp; S for pressure in boundary cells is</span>
<span id="L807">                                ! extrapolated, rather than using PCM in these cells. If true, the same order</span>
<span id="L808">                                ! polynomial is used as is used for the interior cells.</span>
<span id="L809">USE_STANLEY_PGF = False         !   [Boolean] default = False</span>
<span id="L810">                                ! If true, turn on Stanley SGS T variance parameterization in PGF code.</span>
<span id="L811"></span>
<span id="L812">! === module MOM_Zanna_Bolton ===</span>
<span id="L813">USE_ZB2020 = False              !   [Boolean] default = False</span>
<span id="L814">                                ! If true, turns on Zanna-Bolton-2020 (ZB) subgrid momentum parameterization of</span>
<span id="L815">                                ! mesoscale eddies.</span>
<span id="L816"></span>
<span id="L817">! === module MOM_hor_visc ===</span>
<span id="L818">USE_CIRCULATION_IN_HORVISC = False !   [Boolean] default = False</span>
<span id="L819">                                ! Use circulation theorem to compute vorticity in horvisc module (for ZB20 or</span>
<span id="L820">                                ! Leith)</span>
<span id="L821">USE_CONT_THICKNESS = False      !   [Boolean] default = False</span>
<span id="L822">                                ! If true, use thickness at velocity points from continuity solver. This option</span>
<span id="L823">                                ! currently only works with split mode.</span>
<span id="L824">LAPLACIAN = False               !   [Boolean] default = False</span>
<span id="L825">                                ! If true, use a Laplacian horizontal viscosity.</span>
<span id="L826">BIHARMONIC = True               !   [Boolean] default = True</span>
<span id="L827">                                ! If true, use a biharmonic horizontal viscosity. BIHARMONIC may be used with</span>
<span id="L828">                                ! LAPLACIAN.</span>
<span id="L829">AH = 0.0                        !   [m4 s-1] default = 0.0</span>
<span id="L830">                                ! The background biharmonic horizontal viscosity.</span>
<span id="L831">AH_VEL_SCALE = 0.0              !   [m s-1] default = 0.0</span>
<span id="L832">                                ! The velocity scale which is multiplied by the cube of the grid spacing to</span>
<span id="L833">                                ! calculate the biharmonic viscosity. The final viscosity is the largest of this</span>
<span id="L834">                                ! scaled viscosity, the Smagorinsky and Leith viscosities, and AH.</span>
<span id="L835">AH_TIME_SCALE = 0.0             !   [s] default = 0.0</span>
<span id="L836">                                ! A time scale whose inverse is multiplied by the fourth power of the grid</span>
<span id="L837">                                ! spacing to calculate biharmonic viscosity. The final viscosity is the largest</span>
<span id="L838">                                ! of all viscosity formulations in use. 0.0 means that it&#x27;s not used.</span>
<span id="L839">SMAGORINSKY_AH = False          !   [Boolean] default = False</span>
<span id="L840">                                ! If true, use a biharmonic Smagorinsky nonlinear eddy viscosity.</span>
<span id="L841">LEITH_AH = False                !   [Boolean] default = False</span>
<span id="L842">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity.</span>
<span id="L843">USE_LEITHY = False              !   [Boolean] default = False</span>
<span id="L844">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity together with a</span>
<span id="L845">                                ! harmonic backscatter.</span>
<span id="L846">BOUND_AH = True                 !   [Boolean] default = True</span>
<span id="L847">                                ! If true, the biharmonic coefficient is locally limited to be stable.</span>
<span id="L848">RE_AH = 0.0                     !   [nondim] default = 0.0</span>
<span id="L849">                                ! If nonzero, the biharmonic coefficient is scaled so that the biharmonic</span>
<span id="L850">                                ! Reynolds number is equal to this.</span>
<span id="L851">USE_LAND_MASK_FOR_HVISC = True  !   [Boolean] default = True</span>
<span id="L852">                                ! If true, use the land mask for the computation of thicknesses at velocity</span>
<span id="L853">                                ! locations. This eliminates the dependence on arbitrary values over land or</span>
<span id="L854">                                ! outside of the domain.</span>
<span id="L855">HORVISC_BOUND_COEF = 0.8        !   [nondim] default = 0.8</span>
<span id="L856">                                ! The nondimensional coefficient of the ratio of the viscosity bounds to the</span>
<span id="L857">                                ! theoretical maximum for stability without considering other terms.</span>
<span id="L858">FRICTWORK_BUG = False           !   [Boolean] default = False</span>
<span id="L859">                                ! If true, retain an answer-changing bug in calculating the FrictWork, which</span>
<span id="L860">                                ! cancels the h in thickness flux and the h at velocity point. This isnot</span>
<span id="L861">                                ! recommended.</span>
<span id="L862"></span>
<span id="L863">! === module MOM_vert_friction ===</span>
<span id="L864">VERT_FRICTION_ANSWER_DATE = 20181231 ! default = 20181231</span>
<span id="L865">                                ! The vintage of the order of arithmetic and expressions in the viscous</span>
<span id="L866">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L867">                                ! while higher values use expressions that do not use an arbitrary hard-coded</span>
<span id="L868">                                ! maximum viscous coupling coefficient between layers.  Values below 20230601</span>
<span id="L869">                                ! recover a form of the viscosity within the mixed layer that breaks up the</span>
<span id="L870">                                ! magnitude of the wind stress in some non-Boussinesq cases.</span>
<span id="L871">DIRECT_STRESS = False           !   [Boolean] default = False</span>
<span id="L872">                                ! If true, the wind stress is distributed over the topmost HMIX_STRESS of fluid</span>
<span id="L873">                                ! (like in HYCOM), and an added mixed layer viscosity or a physically based</span>
<span id="L874">                                ! boundary layer turbulence parameterization is not needed for stability.</span>
<span id="L875">FIXED_DEPTH_LOTW_ML = False     !   [Boolean] default = False</span>
<span id="L876">                                ! If true, use a Law-of-the-wall prescription for the mixed layer viscosity</span>
<span id="L877">                                ! within a boundary layer that is the lesser of HMIX_FIXED and the total depth</span>
<span id="L878">                                ! of the ocean in a column.</span>
<span id="L879">LOTW_VISCOUS_ML_FLOOR = False   !   [Boolean] default = False</span>
<span id="L880">                                ! If true, use a Law-of-the-wall prescription to set a lower bound on the</span>
<span id="L881">                                ! viscous coupling between layers within the surface boundary layer, based the</span>
<span id="L882">                                ! distance of interfaces from the surface.  This only acts when there are large</span>
<span id="L883">                                ! changes in the thicknesses of successive layers or when the viscosity is set</span>
<span id="L884">                                ! externally and the wind stress has subsequently increased.</span>
<span id="L885">VON_KARMAN_CONST = 0.41         !   [nondim] default = 0.41</span>
<span id="L886">                                ! The value the von Karman constant as used for mixed layer viscosity.</span>
<span id="L887">HARMONIC_VISC = False           !   [Boolean] default = False</span>
<span id="L888">                                ! If true, use the harmonic mean thicknesses for calculating the vertical</span>
<span id="L889">                                ! viscosity.</span>
<span id="L890">HARMONIC_BL_SCALE = 0.0         !   [nondim] default = 0.0</span>
<span id="L891">                                ! A scale to determine when water is in the boundary layers based solely on</span>
<span id="L892">                                ! harmonic mean thicknesses for the purpose of determining the extent to which</span>
<span id="L893">                                ! the thicknesses used in the viscosities are upwinded.</span>
<span id="L894">HMIX_FIXED = 1.0                !   [m]</span>
<span id="L895">                                ! The prescribed depth over which the near-surface viscosity and diffusivity are</span>
<span id="L896">                                ! elevated when the bulk mixed layer is not used.</span>
<span id="L897">USE_GL90_IN_SSW = False         !   [Boolean] default = False</span>
<span id="L898">                                ! If true, use simpler method to calculate 1/N^2 in GL90 vertical viscosity</span>
<span id="L899">                                ! coefficient. This method is valid in stacked shallow water mode.</span>
<span id="L900">KV_ML_INVZ2 = 0.0               !   [m2 s-1] default = 0.0</span>
<span id="L901">                                ! An extra kinematic viscosity in a mixed layer of thickness HMIX_FIXED, with</span>
<span id="L902">                                ! the actual viscosity scaling as 1/(z*HMIX_FIXED)^2, where z is the distance</span>
<span id="L903">                                ! from the surface, to allow for finite wind stresses to be transmitted through</span>
<span id="L904">                                ! infinitesimally thin surface layers.  This is an older option for numerical</span>
<span id="L905">                                ! convenience without a strong physical basis, and its use is now discouraged.</span>
<span id="L906">KV_EXTRA_BBL = 0.0              !   [m2 s-1] default = 0.0</span>
<span id="L907">                                ! An extra kinematic viscosity in the benthic boundary layer. KV_EXTRA_BBL is</span>
<span id="L908">                                ! not used if BOTTOMDRAGLAW is true.</span>
<span id="L909">CFL_TRUNCATE = 0.5              !   [nondim] default = 0.5</span>
<span id="L910">                                ! The value of the CFL number that will cause velocity components to be</span>
<span id="L911">                                ! truncated; instability can occur past 0.5.</span>
<span id="L912">CFL_REPORT = 0.5                !   [nondim] default = 0.5</span>
<span id="L913">                                ! The value of the CFL number that causes accelerations to be reported; the</span>
<span id="L914">                                ! default is CFL_TRUNCATE.</span>
<span id="L915">CFL_TRUNCATE_RAMP_TIME = 0.0    !   [s] default = 0.0</span>
<span id="L916">                                ! The time over which the CFL truncation value is ramped up at the beginning of</span>
<span id="L917">                                ! the run.</span>
<span id="L918">CFL_TRUNCATE_START = 0.0        !   [nondim] default = 0.0</span>
<span id="L919">                                ! The start value of the truncation CFL number used when ramping up CFL_TRUNC.</span>
<span id="L920">STOKES_MIXING_COMBINED = False  !   [Boolean] default = False</span>
<span id="L921">                                ! Flag to use Stokes drift Mixing via the Lagrangian  current (Eulerian plus</span>
<span id="L922">                                ! Stokes drift).  Still needs work and testing, so not recommended for use.</span>
<span id="L923">VEL_UNDERFLOW = 0.0             !   [m s-1] default = 0.0</span>
<span id="L924">                                ! A negligibly small velocity magnitude below which velocity components are set</span>
<span id="L925">                                ! to 0.  A reasonable value might be 1e-30 m/s, which is less than an Angstrom</span>
<span id="L926">                                ! divided by the age of the universe.</span>
<span id="L927"></span>
<span id="L928">! === module MOM_mixed_layer_restrat ===</span>
<span id="L929">MIXEDLAYER_RESTRAT = False      !   [Boolean] default = False</span>
<span id="L930">                                ! If true, a density-gradient dependent re-stratifying flow is imposed in the</span>
<span id="L931">                                ! mixed layer. Can be used in ALE mode without restriction but in layer mode can</span>
<span id="L932">                                ! only be used if BULKMIXEDLAYER is true.</span>
<span id="L933"></span>
<span id="L934">! === module MOM_diagnostics ===</span>
<span id="L935">DIAG_EBT_MONO_N2_COLUMN_FRACTION = 0.0 !   [nondim] default = 0.0</span>
<span id="L936">                                ! The lower fraction of water column over which N2 is limited as monotonic for</span>
<span id="L937">                                ! the purposes of calculating the equivalent barotropic wave speed.</span>
<span id="L938">DIAG_EBT_MONO_N2_DEPTH = -1.0   !   [m] default = -1.0</span>
<span id="L939">                                ! The depth below which N2 is limited as monotonic for the purposes of</span>
<span id="L940">                                ! calculating the equivalent barotropic wave speed.</span>
<span id="L941">INTERNAL_WAVE_SPEED_TOL = 0.001 !   [nondim] default = 0.001</span>
<span id="L942">                                ! The fractional tolerance for finding the wave speeds.</span>
<span id="L943">INTERNAL_WAVE_SPEED_MIN = 0.0   !   [m s-1] default = 0.0</span>
<span id="L944">                                ! A floor in the first mode speed below which 0 used instead.</span>
<span id="L945">INTERNAL_WAVE_SPEED_BETTER_EST = True !   [Boolean] default = True</span>
<span id="L946">                                ! If true, use a more robust estimate of the first mode wave speed as the</span>
<span id="L947">                                ! starting point for iterations.</span>
<span id="L948">INTWAVE_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L949">                                ! If true, use the OM4 remapping-via-subcells algorithm for calculating EBT</span>
<span id="L950">                                ! structure. See REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting</span>
<span id="L951">                                ! this option to false.</span>
<span id="L952"></span>
<span id="L953">! === module MOM_diabatic_driver ===</span>
<span id="L954">! The following parameters are used for diabatic processes.</span>
<span id="L955"></span>
<span id="L956">! === module MOM_tracer_advect ===</span>
<span id="L957">TRACER_ADVECTION_SCHEME = &quot;PLM&quot; ! default = &quot;PLM&quot;</span>
<span id="L958">                                ! The horizontal transport scheme for tracers:</span>
<span id="L959">                                !   PLM    - Piecewise Linear Method</span>
<span id="L960">                                !   PPM:H3 - Piecewise Parabolic Method (Huyhn 3rd order)</span>
<span id="L961">                                !   PPM    - Piecewise Parabolic Method (Colella-Woodward)</span>
<span id="L962"></span>
<span id="L963">! === module MOM_tracer_hor_diff ===</span>
<span id="L964">KHTR = 0.0                      !   [m2 s-1] default = 0.0</span>
<span id="L965">                                ! The background along-isopycnal tracer diffusivity.</span>
<span id="L966">KHTR_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L967">                                ! The minimum along-isopycnal tracer diffusivity.</span>
<span id="L968">KHTR_MAX = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L969">                                ! The maximum along-isopycnal tracer diffusivity. Set to a positive value to</span>
<span id="L970">                                ! activate.</span>
<span id="L971">KHTR_PASSIVITY_COEFF = 0.0      !   [nondim] default = 0.0</span>
<span id="L972">                                ! The coefficient that scales deformation radius over grid-spacing in passivity,</span>
<span id="L973">                                ! where passivity is the ratio between along isopycnal mixing of tracers to</span>
<span id="L974">                                ! thickness mixing. A non-zero value enables this parameterization.</span>
<span id="L975">KHTR_PASSIVITY_MIN = 0.5        !   [nondim] default = 0.5</span>
<span id="L976">                                ! The minimum passivity which is the ratio between along isopycnal mixing of</span>
<span id="L977">                                ! tracers to thickness mixing.</span>
<span id="L978">DIFFUSE_ML_TO_INTERIOR = False  !   [Boolean] default = False</span>
<span id="L979">                                ! If true, enable epipycnal mixing between the surface boundary layer and the</span>
<span id="L980">                                ! interior.</span>
<span id="L981">CHECK_DIFFUSIVE_CFL = False     !   [Boolean] default = False</span>
<span id="L982">                                ! If true, use enough iterations the diffusion to ensure that the diffusive</span>
<span id="L983">                                ! equivalent of the CFL limit is not violated.  If false, always use the greater</span>
<span id="L984">                                ! of 1 or MAX_TR_DIFFUSION_CFL iteration.</span>
<span id="L985">MAX_TR_DIFFUSION_CFL = -1.0     !   [nondim] default = -1.0</span>
<span id="L986">                                ! If positive, locally limit the along-isopycnal tracer diffusivity to keep the</span>
<span id="L987">                                ! diffusive CFL locally at or below this value.  The number of diffusive</span>
<span id="L988">                                ! iterations is often this value or the next greater integer.</span>
<span id="L989">RECALC_NEUTRAL_SURF = False     !   [Boolean] default = False</span>
<span id="L990">                                ! If true, then recalculate the neutral surfaces if the</span>
<span id="L991">                                ! diffusive CFL is exceeded. If false, assume that the</span>
<span id="L992">                                ! positions of the surfaces do not change</span>
<span id="L993"></span>
<span id="L994">! === module MOM_neutral_diffusion ===</span>
<span id="L995">! This module implements neutral diffusion of tracers</span>
<span id="L996">USE_NEUTRAL_DIFFUSION = False   !   [Boolean] default = False</span>
<span id="L997">                                ! If true, enables the neutral diffusion module.</span>
<span id="L998"></span>
<span id="L999">! === module MOM_hor_bnd_diffusion ===</span>
<span id="L1000">! This module implements horizontal diffusion of tracers near boundaries</span>
<span id="L1001">USE_HORIZONTAL_BOUNDARY_DIFFUSION = False !   [Boolean] default = False</span>
<span id="L1002">                                ! If true, enables the horizonal boundary tracer&#x27;s diffusion module.</span>
<span id="L1003">OBSOLETE_DIAGNOSTIC_IS_FATAL = True !   [Boolean] default = True</span>
<span id="L1004">                                ! If an obsolete diagnostic variable appears in the diag_table, cause a FATAL</span>
<span id="L1005">                                ! error rather than issue a WARNING.</span>
<span id="L1006"></span>
<span id="L1007">! === module MOM_sum_output ===</span>
<span id="L1008">CALCULATE_APE = True            !   [Boolean] default = True</span>
<span id="L1009">                                ! If true, calculate the available potential energy of the interfaces.  Setting</span>
<span id="L1010">                                ! this to false reduces the memory footprint of high-PE-count models</span>
<span id="L1011">                                ! dramatically.</span>
<span id="L1012">WRITE_STOCKS = True             !   [Boolean] default = True</span>
<span id="L1013">                                ! If true, write the integrated tracer amounts to stdout when the energy files</span>
<span id="L1014">                                ! are written.</span>
<span id="L1015">MAXTRUNC = 0                    !   [truncations save_interval-1] default = 0</span>
<span id="L1016">                                ! The run will be stopped, and the day set to a very large value if the velocity</span>
<span id="L1017">                                ! is truncated more than MAXTRUNC times between energy saves.  Set MAXTRUNC to 0</span>
<span id="L1018">                                ! to stop if there is any truncation of velocities.</span>
<span id="L1019">MAX_ENERGY = 0.0                !   [m2 s-2] default = 0.0</span>
<span id="L1020">                                ! The maximum permitted average energy per unit mass; the model will be stopped</span>
<span id="L1021">                                ! if there is more energy than this.  If zero or negative, this is set to</span>
<span id="L1022">                                ! 10*MAXVEL^2.</span>
<span id="L1023">MAXVEL = 3.0E+08                !   [m s-1] default = 3.0E+08</span>
<span id="L1024">                                ! The maximum velocity allowed before the velocity components are truncated.</span>
<span id="L1025">ENERGYFILE = &quot;ocean.stats&quot;      ! default = &quot;ocean.stats&quot;</span>
<span id="L1026">                                ! The file to use to write the energies and globally summed diagnostics.</span>
<span id="L1027">DATE_STAMPED_STDOUT = True      !   [Boolean] default = True</span>
<span id="L1028">                                ! If true, use dates (not times) in messages to stdout</span>
<span id="L1029">ISO_DATE_STAMPED_STDOUT = False !   [Boolean] default = False</span>
<span id="L1030">                                ! If true, use ISO formatted dates in messages to stdout</span>
<span id="L1031">TIMEUNIT = 8.64E+04             !   [s] default = 8.64E+04</span>
<span id="L1032">                                ! The time unit in seconds a number of input fields</span>
<span id="L1033">READ_DEPTH_LIST = False         !   [Boolean] default = False</span>
<span id="L1034">                                ! Read the depth list from a file if it exists or create that file otherwise.</span>
<span id="L1035">DEPTH_LIST_MIN_INC = 1.0E-10    !   [m] default = 1.0E-10</span>
<span id="L1036">                                ! The minimum increment between the depths of the entries in the depth-list</span>
<span id="L1037">                                ! file.</span>
<span id="L1038">ENERGYSAVEDAYS = 1.0            !   [days] default = 1.0</span>
<span id="L1039">                                ! The interval in units of TIMEUNIT between saves of the energies of the run and</span>
<span id="L1040">                                ! other globally summed diagnostics.</span>
<span id="L1041">ENERGYSAVEDAYS_GEOMETRIC = 0.0  !   [days] default = 0.0</span>
<span id="L1042">                                ! The starting interval in units of TIMEUNIT for the first call to save the</span>
<span id="L1043">                                ! energies of the run and other globally summed diagnostics. The interval</span>
<span id="L1044">                                ! increases by a factor of 2. after each call to write_energy.</span>
<span id="L1045"></span>
<span id="L1046">! === module ocean_stochastics_init ===</span>
<span id="L1047">DO_SPPT = False                 !   [Boolean] default = False</span>
<span id="L1048">                                ! If true, then stochastically perturb the thermodynamic tendencies of T,S, amd</span>
<span id="L1049">                                ! h.  Amplitude and correlations are controlled by the nam_stoch namelist in the</span>
<span id="L1050">                                ! UFS model only.</span>
<span id="L1051">DO_SKEB = False                 !   [Boolean] default = False</span>
<span id="L1052">                                ! If true, then stochastically perturb the currents using the stochastic kinetic</span>
<span id="L1053">                                ! energy backscatter scheme.</span>
<span id="L1054">PERT_EPBL = False               !   [Boolean] default = False</span>
<span id="L1055">                                ! If true, then stochastically perturb the kinetic energy production and</span>
<span id="L1056">                                ! dissipation terms.  Amplitude and correlations are controlled by the nam_stoch</span>
<span id="L1057">                                ! namelist in the UFS model only.</span>
<span id="L1058"></span>
<span id="L1059">! === module MOM_surface_forcing ===</span>
<span id="L1060">VARIABLE_WINDS = True           !   [Boolean] default = True</span>
<span id="L1061">                                ! If true, the winds vary in time after the initialization.</span>
<span id="L1062">VARIABLE_BUOYFORCE = True       !   [Boolean] default = True</span>
<span id="L1063">                                ! If true, the buoyancy forcing varies in time after the initialization of the</span>
<span id="L1064">                                ! model.</span>
<span id="L1065">BUOY_CONFIG = &quot;zero&quot;            ! default = &quot;zero&quot;</span>
<span id="L1066">                                ! The character string that indicates how buoyancy forcing is specified.  Valid</span>
<span id="L1067">                                ! options include (file), (data_override), (zero), (const), (linear), (MESO),</span>
<span id="L1068">                                ! (SCM_CVmix_tests), (BFB), (dumbbell), (USER) and (NONE).</span>
<span id="L1069">WIND_CONFIG = &quot;zero&quot;            ! default = &quot;zero&quot;</span>
<span id="L1070">                                ! The character string that indicates how wind forcing is specified.  Valid</span>
<span id="L1071">                                ! options include (file), (data_override), (2gyre), (1gyre), (gyres), (zero),</span>
<span id="L1072">                                ! (const), (Neverworld), (scurves), (ideal_hurr), (SCM_CVmix_tests) and (USER).</span>
<span id="L1073">RESTOREBUOY = False             !   [Boolean] default = False</span>
<span id="L1074">                                ! If true, the buoyancy fluxes drive the model back toward some specified</span>
<span id="L1075">                                ! surface state with a rate given by FLUXCONST.</span>
<span id="L1076">LATENT_HEAT_FUSION = 3.34E+05   !   [J/kg] default = 3.34E+05</span>
<span id="L1077">                                ! The latent heat of fusion.</span>
<span id="L1078">LATENT_HEAT_VAPORIZATION = 2.5E+06 !   [J/kg] default = 2.5E+06</span>
<span id="L1079">                                ! The latent heat of fusion.</span>
<span id="L1080">GUST_CONST = 0.0                !   [Pa] default = 0.0</span>
<span id="L1081">                                ! The background gustiness in the winds.</span>
<span id="L1082">USTAR_GUSTLESS_BUG = False      !   [Boolean] default = False</span>
<span id="L1083">                                ! If true include a bug in the time-averaging of the gustless wind friction</span>
<span id="L1084">                                ! velocity</span>
<span id="L1085">READ_GUST_2D = False            !   [Boolean] default = False</span>
<span id="L1086">                                ! If true, use a 2-dimensional gustiness supplied from an input file</span>
<span id="L1087"></span>
<span id="L1088">! === module MOM_restart ===</span>
<span id="L1089">USE_WAVES = False               !   [Boolean] default = False</span>
<span id="L1090">                                ! If true, enables surface wave modules.</span>
<span id="L1091"></span>
<span id="L1092">! === module MOM_main (MOM_driver) ===</span>
<span id="L1093">DT_FORCING = 8.64E+04           !   [s] default = 8.64E+04</span>
<span id="L1094">                                ! The time step for changing forcing, coupling with other components, or</span>
<span id="L1095">                                ! potentially writing certain diagnostics. The default value is given by DT.</span>
<span id="L1096">DAYMAX = 1.0                    !   [days]</span>
<span id="L1097">                                ! The final time of the whole simulation, in units of TIMEUNIT seconds.  This</span>
<span id="L1098">                                ! also sets the potential end time of the present run segment if the end time is</span>
<span id="L1099">                                ! not set via ocean_solo_nml in input.nml.</span>
<span id="L1100">SINGLE_STEPPING_CALL = True     !   [Boolean] default = True</span>
<span id="L1101">                                ! If true, advance the state of MOM with a single step including both dynamics</span>
<span id="L1102">                                ! and thermodynamics.  If false the two phases are advanced with separate calls.</span>
<span id="L1103">RESTART_CONTROL = 1             ! default = 1</span>
<span id="L1104">                                ! An integer whose bits encode which restart files are written. Add 2 (bit 1)</span>
<span id="L1105">                                ! for a time-stamped file, and odd (bit 0) for a non-time-stamped file. A</span>
<span id="L1106">                                ! non-time-stamped restart file is saved at the end of the run segment for any</span>
<span id="L1107">                                ! non-negative value.</span>
<span id="L1108">RESTINT = 0.0                   !   [days] default = 0.0</span>
<span id="L1109">                                ! The interval between saves of the restart file in units of TIMEUNIT.  Use 0</span>
<span id="L1110">                                ! (the default) to not save incremental restart files at all.</span>
<span id="L1111">WRITE_CPU_STEPS = 1000          ! default = 1000</span>
<span id="L1112">                                ! The number of coupled timesteps between writing the cpu time. If this is not</span>
<span id="L1113">                                ! positive, do not check cpu time, and the segment run-length can not be set via</span>
<span id="L1114">                                ! an elapsed CPU time.</span>
<span id="L1115"></span>
<span id="L1116">! === module MOM_write_cputime ===</span>
<span id="L1117">MAXCPU = -1.0                   !   [wall-clock seconds] default = -1.0</span>
<span id="L1118">                                ! The maximum amount of cpu time per processor for which MOM should run before</span>
<span id="L1119">                                ! saving a restart file and quitting with a return value that indicates that a</span>
<span id="L1120">                                ! further run is required to complete the simulation. If automatic restarts are</span>
<span id="L1121">                                ! not desired, use a negative value for MAXCPU.  MAXCPU has units of wall-clock</span>
<span id="L1122">                                ! seconds, so the actual CPU time used is larger by a factor of the number of</span>
<span id="L1123">                                ! processors used.</span>
<span id="L1124">CPU_TIME_FILE = &quot;CPU_stats&quot;     ! default = &quot;CPU_stats&quot;</span>
<span id="L1125">                                ! The file into which CPU time is written.</span>
<span id="L1126"></span>
<span id="L1127">! === module MOM_file_parser ===</span>
<span id="L1128">SEND_LOG_TO_STDOUT = False      !   [Boolean] default = False</span>
<span id="L1129">                                ! If true, all log messages are also sent to stdout.</span>
<span id="L1130">DOCUMENT_FILE = &quot;MOM_parameter_doc&quot; ! default = &quot;MOM_parameter_doc&quot;</span>
<span id="L1131">                                ! The basename for files where run-time parameters, their settings, units and</span>
<span id="L1132">                                ! defaults are documented. Blank will disable all parameter documentation.</span>
<span id="L1133">COMPLETE_DOCUMENTATION = True   !   [Boolean] default = True</span>
<span id="L1134">                                ! If true, all run-time parameters are documented in MOM_parameter_doc.all .</span>
<span id="L1135">MINIMAL_DOCUMENTATION = True    !   [Boolean] default = True</span>
<span id="L1136">                                ! If true, non-default run-time parameters are documented in</span>
<span id="L1137">                                ! MOM_parameter_doc.short .</span>
</pre>
