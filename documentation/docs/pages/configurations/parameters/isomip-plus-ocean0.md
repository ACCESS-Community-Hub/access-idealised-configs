---
search:
  exclude: true
---

# isomip-plus-ocean0: MOM_parameter_doc.all

Every MOM6 parameter of the tested run of [isomip-plus-ocean0](../isomip-plus.md), as MOM6 wrote it to `MOM_parameter_doc.all` in the run's output folder. Line numbers match the file.

<pre class="paramdoc"><span id="L1">! This file was written by the model and records all non-layout or debugging parameters used at run-time.</span>
<span id="L2"></span>
<span id="L3">! === module MOM ===</span>
<span id="L4">SPLIT = True                    !   [Boolean] default = True</span>
<span id="L5">                                ! Use the split time stepping if true.</span>
<span id="L6">SPLIT_RK2B = False              !   [Boolean] default = False</span>
<span id="L7">                                ! If true, use a version of the split explicit time stepping scheme that</span>
<span id="L8">                                ! exchanges velocities with step_MOM that have the average barotropic phase over</span>
<span id="L9">                                ! a baroclinic timestep rather than the instantaneous barotropic phase.</span>
<span id="L10">CALC_RHO_FOR_SEA_LEVEL = False  !   [Boolean] default = False</span>
<span id="L11">                                ! If true, the in-situ density is used to calculate the effective sea level that</span>
<span id="L12">                                ! is returned to the coupler. If false, the Boussinesq parameter RHO_0 is used.</span>
<span id="L13">ENABLE_THERMODYNAMICS = True    !   [Boolean] default = True</span>
<span id="L14">                                ! If true, Temperature and salinity are used as state variables.</span>
<span id="L15">USE_EOS = True                  !   [Boolean] default = True</span>
<span id="L16">                                ! If true,  density is calculated from temperature and salinity with an equation</span>
<span id="L17">                                ! of state.  If USE_EOS is true, ENABLE_THERMODYNAMICS must be true as well.</span>
<span id="L18">DIABATIC_FIRST = False          !   [Boolean] default = False</span>
<span id="L19">                                ! If true, apply diabatic and thermodynamic processes, including buoyancy</span>
<span id="L20">                                ! forcing and mass gain or loss, before stepping the dynamics forward.</span>
<span id="L21">USE_CONTEMP_ABSSAL = False      !   [Boolean] default = False</span>
<span id="L22">                                ! If true, the prognostics T&amp;S are the conservative temperature and absolute</span>
<span id="L23">                                ! salinity. Care should be taken to convert them to potential temperature and</span>
<span id="L24">                                ! practical salinity before exchanging them with the coupler and/or reporting</span>
<span id="L25">                                ! T&amp;S diagnostics.</span>
<span id="L26">ADIABATIC = False               !   [Boolean] default = False</span>
<span id="L27">                                ! There are no diapycnal mass fluxes if ADIABATIC is true.  This assumes that KD</span>
<span id="L28">                                ! = 0.0 and that there is no buoyancy forcing, but makes the model faster by</span>
<span id="L29">                                ! eliminating subroutine calls.</span>
<span id="L30">DO_DYNAMICS = True              !   [Boolean] default = True</span>
<span id="L31">                                ! If False, skips the dynamics calls that update u &amp; v, as well as the gravity</span>
<span id="L32">                                ! wave adjustment to h. This may be a fragile feature, but can be useful during</span>
<span id="L33">                                ! development</span>
<span id="L34">OFFLINE_TRACER_MODE = False     !   [Boolean] default = False</span>
<span id="L35">                                ! If true, barotropic and baroclinic dynamics, thermodynamics are all bypassed</span>
<span id="L36">                                ! with all the fields necessary to integrate the tracer advection and diffusion</span>
<span id="L37">                                ! equation are read in from files stored from a previous integration of the</span>
<span id="L38">                                ! prognostic model. NOTE: This option only used in the ocean_solo_driver.</span>
<span id="L39">USE_REGRIDDING = True           !   [Boolean] default = False</span>
<span id="L40">                                ! If True, use the ALE algorithm (regridding/remapping). If False, use the</span>
<span id="L41">                                ! layered isopycnal algorithm.</span>
<span id="L42">REMAP_UV_USING_OLD_ALG = False  !   [Boolean] default = False</span>
<span id="L43">                                ! If true, uses the old remapping-via-a-delta-z method for remapping u and v. If</span>
<span id="L44">                                ! false, uses the new method that remaps between grids described by an old and</span>
<span id="L45">                                ! new thickness.</span>
<span id="L46">REMAP_AUXILIARY_VARS = False    !   [Boolean] default = False</span>
<span id="L47">                                ! If true, apply ALE remapping to all of the auxiliary 3-dimensional variables</span>
<span id="L48">                                ! that are needed to reproduce across restarts, similarly to what is already</span>
<span id="L49">                                ! being done with the primary state variables.  The default should be changed to</span>
<span id="L50">                                ! true.</span>
<span id="L51">BULKMIXEDLAYER = False          !   [Boolean] default = False</span>
<span id="L52">                                ! If true, use a Kraus-Turner-like bulk mixed layer with transitional buffer</span>
<span id="L53">                                ! layers.  Layers 1 through NKML+NKBL have variable densities. There must be at</span>
<span id="L54">                                ! least NKML+NKBL+1 layers if BULKMIXEDLAYER is true. BULKMIXEDLAYER can not be</span>
<span id="L55">                                ! used with USE_REGRIDDING. The default is influenced by ENABLE_THERMODYNAMICS.</span>
<span id="L56">USE_POROUS_BARRIER = False      !   [Boolean] default = False</span>
<span id="L57">                                ! If true, use porous barrier to constrain the widths and face areas at the</span>
<span id="L58">                                ! edges of the grid cells.</span>
<span id="L59">BATHYMETRY_AT_VEL = False       !   [Boolean] default = False</span>
<span id="L60">                                ! If true, there are separate values for the basin depths at velocity points.</span>
<span id="L61">                                ! Otherwise the effects of topography are entirely determined from thickness</span>
<span id="L62">                                ! points.</span>
<span id="L63">ENABLE_BUGS_BY_DEFAULT = True   !   [Boolean] default = True</span>
<span id="L64">                                ! If true, the defaults for certain recently added bug-fix flags are set to</span>
<span id="L65">                                ! recreate the bugs so that the code can be moved forward without changing</span>
<span id="L66">                                ! answers for existing configurations.  The defaults for groups of bug-fix flags</span>
<span id="L67">                                ! are periodcially changed to correct the bugs, at which point this parameter</span>
<span id="L68">                                ! will no longer be used to set their default.  Setting this to false means that</span>
<span id="L69">                                ! bugs are only used if they are actively selected, but it also means that</span>
<span id="L70">                                ! answers may change when code is updated due to newly found bugs.</span>
<span id="L71">DT = 720.0                      !   [s]</span>
<span id="L72">                                ! The (baroclinic) dynamics time step.  The time-step that is actually used will</span>
<span id="L73">                                ! be an integer fraction of the forcing time-step (DT_FORCING in ocean-only mode</span>
<span id="L74">                                ! or the coupling timestep in coupled mode.)</span>
<span id="L75">DT_THERM = 720.0                !   [s] default = 720.0</span>
<span id="L76">                                ! The thermodynamic time step. Ideally DT_THERM should be an integer multiple of</span>
<span id="L77">                                ! DT and of DT_TRACER_ADVECT and less than the forcing or coupling time-step.</span>
<span id="L78">                                ! However, if THERMO_SPANS_COUPLING is true, DT_THERM can be an integer multiple</span>
<span id="L79">                                ! of the coupling timestep. By default DT_THERM is set to DT.</span>
<span id="L80">THERMO_SPANS_COUPLING = False   !   [Boolean] default = False</span>
<span id="L81">                                ! If true, the MOM will take thermodynamic timesteps that can be longer than the</span>
<span id="L82">                                ! coupling timestep. The actual thermodynamic timestep that is used in this case</span>
<span id="L83">                                ! is the largest integer multiple of the coupling timestep that is less than or</span>
<span id="L84">                                ! equal to DT_THERM.</span>
<span id="L85">DT_TRACER_ADVECT = 720.0        !   [s] default = 720.0</span>
<span id="L86">                                ! The tracer advection time step. Ideally DT_TRACER_ADVECT should be an integer</span>
<span id="L87">                                ! multiple of DT, less than DT_THERM, and less than the forcing or coupling</span>
<span id="L88">                                ! time-step. However, if TRADV_SPANS_COUPLING is true, DT_TRACER_ADVECT can be</span>
<span id="L89">                                ! longer than the coupling timestep. By default DT_TRACER_ADVECT is set to</span>
<span id="L90">                                ! DT_THERM.</span>
<span id="L91">TRADV_SPANS_COUPLING = False    !   [Boolean] default = False</span>
<span id="L92">                                ! If true, the MOM will take tracer advection timesteps that can be longer than</span>
<span id="L93">                                ! the coupling timestep. The actual tracer advection timestep that is used in</span>
<span id="L94">                                ! this case is the largest integer multiple of the coupling timestep that is</span>
<span id="L95">                                ! less than or equal to DT_TRACER_ADVECT.</span>
<span id="L96">THICKNESSDIFFUSE = False        !   [Boolean] default = False</span>
<span id="L97">                                ! If true, isopycnal surfaces are diffused with a Laplacian coefficient of KHTH.</span>
<span id="L98">APPLY_INTERFACE_FILTER = False  !   [Boolean] default = False</span>
<span id="L99">                                ! If true, model interface heights are subjected to a grid-scale dependent</span>
<span id="L100">                                ! spatial smoothing, often with biharmonic filter.</span>
<span id="L101">HMIX_SFC_PROP = 1.0             !   [m] default = 1.0</span>
<span id="L102">                                ! If BULKMIXEDLAYER is false, HMIX_SFC_PROP is the depth over which to average</span>
<span id="L103">                                ! to find surface properties like SST and SSS or density (but not surface</span>
<span id="L104">                                ! velocities).</span>
<span id="L105">HMIX_UV_SFC_PROP = 0.0          !   [m] default = 0.0</span>
<span id="L106">                                ! If BULKMIXEDLAYER is false, HMIX_UV_SFC_PROP is the depth over which to</span>
<span id="L107">                                ! average to find surface flow properties, SSU, SSV. A non-positive value</span>
<span id="L108">                                ! indicates no averaging.</span>
<span id="L109">HFREEZE = -1.0                  !   [m] default = -1.0</span>
<span id="L110">                                ! If HFREEZE &gt; 0, melt potential will be computed. The actual depth over which</span>
<span id="L111">                                ! melt potential is computed will be min(HFREEZE, OBLD), where OBLD is the</span>
<span id="L112">                                ! boundary layer depth. If HFREEZE &lt;= 0 (default), melt potential will not be</span>
<span id="L113">                                ! computed.</span>
<span id="L114">INTERPOLATE_P_SURF = False      !   [Boolean] default = False</span>
<span id="L115">                                ! If true, linearly interpolate the surface pressure over the coupling time</span>
<span id="L116">                                ! step, using the specified value at the end of the step.</span>
<span id="L117">DTBT_RESET_PERIOD = 0.0         !   [s] default = 720.0</span>
<span id="L118">                                ! The period between recalculations of DTBT (if DTBT &lt;= 0). If DTBT_RESET_PERIOD</span>
<span id="L119">                                ! is negative, DTBT is set based only on information available at</span>
<span id="L120">                                ! initialization.  If 0, DTBT will be set every dynamics time step. The default</span>
<span id="L121">                                ! is set by DT_THERM.  This is only used if SPLIT is true.</span>
<span id="L122">FRAZIL = False                  !   [Boolean] default = False</span>
<span id="L123">                                ! If true, water freezes if it gets too cold, and the accumulated heat deficit</span>
<span id="L124">                                ! is returned in the surface state.  FRAZIL is only used if</span>
<span id="L125">                                ! ENABLE_THERMODYNAMICS is true.</span>
<span id="L126">DO_GEOTHERMAL = False           !   [Boolean] default = False</span>
<span id="L127">                                ! If true, apply geothermal heating.</span>
<span id="L128">BOUND_SALINITY = False          !   [Boolean] default = False</span>
<span id="L129">                                ! If true, limit salinity to being positive. (The sea-ice model may ask for more</span>
<span id="L130">                                ! salt than is available and drive the salinity negative otherwise.)</span>
<span id="L131">SALINITY_UNDERFLOW = 0.0        !   [PPT] default = 0.0</span>
<span id="L132">                                ! A tiny value of salinity below which the it is set to 0.  For reference, one</span>
<span id="L133">                                ! molecule of salt per square meter of ocean is of order 1e-29 ppt.</span>
<span id="L134">TEMPERATURE_UNDERFLOW = 0.0     !   [degC] default = 0.0</span>
<span id="L135">                                ! A tiny magnitude of temperatures below which they are set to 0.</span>
<span id="L136">C_P = 3925.0                    !   [J kg-1 K-1] default = 3991.86795711963</span>
<span id="L137">                                ! The heat capacity of sea water, approximated as a constant. This is only used</span>
<span id="L138">                                ! if ENABLE_THERMODYNAMICS is true. The default value is from the TEOS-10</span>
<span id="L139">                                ! definition of conservative temperature.</span>
<span id="L140">USE_PSURF_IN_EOS = True         !   [Boolean] default = True</span>
<span id="L141">                                ! If true, always include the surface pressure contributions in equation of</span>
<span id="L142">                                ! state calculations.</span>
<span id="L143">P_REF = 2.0E+07                 !   [Pa] default = 2.0E+07</span>
<span id="L144">                                ! The pressure that is used for calculating the coordinate density.  (1 Pa = 1e4</span>
<span id="L145">                                ! dbar, so 2e7 is commonly used.) This is only used if USE_EOS and</span>
<span id="L146">                                ! ENABLE_THERMODYNAMICS are true.</span>
<span id="L147">NONBLOCKING_P_SURF_BUG = True   !   [Boolean] default = True</span>
<span id="L148">                                ! If true, recover a bug in which the non-blocking halo update of the surface</span>
<span id="L149">                                ! pressure is not completed before the halo points of forces%p_surf are copied</span>
<span id="L150">                                ! into tv%p_surf, so that those halo points hold the surface pressure from the</span>
<span id="L151">                                ! previous coupling step, or zeros on the first step after a restart.  This is</span>
<span id="L152">                                ! only used if NONBLOCKING_UPDATES and USE_PSURF_IN_EOS are true</span>
<span id="L153">FIRST_DIRECTION = 0             ! default = 0</span>
<span id="L154">                                ! An integer that indicates which direction goes first in parts of the code that</span>
<span id="L155">                                ! use directionally split updates, with even numbers (or 0) used for x- first</span>
<span id="L156">                                ! and odd numbers used for y-first.</span>
<span id="L157">ALTERNATE_FIRST_DIRECTION = False !   [Boolean] default = False</span>
<span id="L158">                                ! If true, after every dynamic timestep alternate whether the x- or y- direction</span>
<span id="L159">                                ! updates occur first in directionally split parts of the calculation. If this</span>
<span id="L160">                                ! is true, FIRST_DIRECTION applies at the start of a new run or if the next</span>
<span id="L161">                                ! first direction can not be found in the restart file.</span>
<span id="L162">CHECK_BAD_SURFACE_VALS = False  !   [Boolean] default = False</span>
<span id="L163">                                ! If true, check the surface state for ridiculous values.</span>
<span id="L164">DEFAULT_ANSWER_DATE = 99991231  ! default = 99991231</span>
<span id="L165">                                ! This sets the default value for the various _ANSWER_DATE parameters.</span>
<span id="L166">SURFACE_ANSWER_DATE = 99991231  ! default = 99991231</span>
<span id="L167">                                ! The vintage of the expressions for the surface properties.  Values below</span>
<span id="L168">                                ! 20190101 recover the answers from the end of 2018, while higher values use</span>
<span id="L169">                                ! updated and more robust forms of the same expressions.</span>
<span id="L170">SAVE_INITIAL_CONDS = True       !   [Boolean] default = False</span>
<span id="L171">                                ! If true, write the initial conditions to a file given by IC_OUTPUT_FILE.</span>
<span id="L172">IC_OUTPUT_FILE = &quot;ISOMIP_IC&quot;    ! default = &quot;MOM_IC&quot;</span>
<span id="L173">                                ! The file into which to write the initial conditions.</span>
<span id="L174">WRITE_GEOM = 1                  ! default = 1</span>
<span id="L175">                                ! If =0, never write the geometry and vertical grid files. If =1, write the</span>
<span id="L176">                                ! geometry and vertical grid files only for a new simulation. If =2, always</span>
<span id="L177">                                ! write the geometry and vertical grid files. Other values are invalid.</span>
<span id="L178">GEOM_FILE = &quot;ocean_geometry&quot;    ! default = &quot;ocean_geometry&quot;</span>
<span id="L179">                                ! The file into which to write the ocean geometry.</span>
<span id="L180">USE_DBCLIENT = False            !   [Boolean] default = False</span>
<span id="L181">                                ! If true, initialize a client to a remote database that can be used for online</span>
<span id="L182">                                ! analysis and machine-learning inference.</span>
<span id="L183">ICE_SHELF = True                !   [Boolean] default = False</span>
<span id="L184">                                ! If true, enables the ice shelf model.</span>
<span id="L185">USE_PARTICLES = False           !   [Boolean] default = False</span>
<span id="L186">                                ! If true, use the particles package.</span>
<span id="L187">USE_UH_PARTICLES = False        !   [Boolean] default = False</span>
<span id="L188">                                ! If true, use the uh velocity in the particles package.</span>
<span id="L189">ENSEMBLE_OCEAN = False          !   [Boolean] default = False</span>
<span id="L190">                                ! If False, The model is being run in serial mode as a single realization. If</span>
<span id="L191">                                ! True, The current model realization is part of a larger ensemble and at the</span>
<span id="L192">                                ! end of step MOM, we will perform a gather of the ensemble members for</span>
<span id="L193">                                ! statistical evaluation and/or data assimilation.</span>
<span id="L194">HOMOGENIZE_FORCINGS = False     !   [Boolean] default = False</span>
<span id="L195">                                ! If True, homogenize the forces and fluxes.</span>
<span id="L196"></span>
<span id="L197">! === module MOM_domains ===</span>
<span id="L198">REENTRANT_X = False             !   [Boolean] default = True</span>
<span id="L199">                                ! If true, the domain is zonally reentrant.</span>
<span id="L200">REENTRANT_Y = False             !   [Boolean] default = False</span>
<span id="L201">                                ! If true, the domain is meridionally reentrant.</span>
<span id="L202">TRIPOLAR_N = False              !   [Boolean] default = False</span>
<span id="L203">                                ! Use tripolar connectivity at the northern edge of the domain.  With</span>
<span id="L204">                                ! TRIPOLAR_N, NIGLOBAL must be even.</span>
<span id="L205">NIGLOBAL = 240                  !</span>
<span id="L206">                                ! The total number of thickness grid points in the x-direction in the physical</span>
<span id="L207">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L208">NJGLOBAL = 40                   !</span>
<span id="L209">                                ! The total number of thickness grid points in the y-direction in the physical</span>
<span id="L210">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L211">NIHALO = 4                      ! default = 4</span>
<span id="L212">                                ! The number of halo points on each side in the x-direction.  How this is set</span>
<span id="L213">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L214">NJHALO = 4                      ! default = 4</span>
<span id="L215">                                ! The number of halo points on each side in the y-direction.  How this is set</span>
<span id="L216">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L217"></span>
<span id="L218">! === module MOM_hor_index ===</span>
<span id="L219">! Sets the horizontal array index types.</span>
<span id="L220"></span>
<span id="L221">! === module MOM_grid ===</span>
<span id="L222">! Parameters providing information about the lateral grid.</span>
<span id="L223">REFERENCE_HEIGHT = 0.0          !   [m] default = 0.0</span>
<span id="L224">                                ! A reference value for geometric height fields, such as bathyT.</span>
<span id="L225"></span>
<span id="L226">! === module MOM_fixed_initialization ===</span>
<span id="L227">INPUTDIR = &quot;INPUT&quot;              ! default = &quot;.&quot;</span>
<span id="L228">                                ! The directory in which input files are found.</span>
<span id="L229"></span>
<span id="L230">! === module MOM_grid_init ===</span>
<span id="L231">GRID_CONFIG = &quot;cartesian&quot;       !</span>
<span id="L232">                                ! A character string that determines the method for defining the horizontal</span>
<span id="L233">                                ! grid.  Current options are:</span>
<span id="L234">                                !     mosaic - read the grid from a mosaic (supergrid)</span>
<span id="L235">                                !              file set by GRID_FILE.</span>
<span id="L236">                                !     cartesian - use a (flat) Cartesian grid.</span>
<span id="L237">                                !     spherical - use a simple spherical grid.</span>
<span id="L238">                                !     mercator - use a Mercator spherical grid.</span>
<span id="L239">AXIS_UNITS = &quot;k&quot;                ! default = &quot;degrees&quot;</span>
<span id="L240">                                ! The units for the Cartesian axes. Valid entries are:</span>
<span id="L241">                                !     degrees - degrees of latitude and longitude</span>
<span id="L242">                                !     m or meter(s) - meters</span>
<span id="L243">                                !     k or km or kilometer(s) - kilometers</span>
<span id="L244">SOUTHLAT = 0.0                  !   [km]</span>
<span id="L245">                                ! The southern latitude of the domain or the equivalent starting value for the</span>
<span id="L246">                                ! y-axis.</span>
<span id="L247">LENLAT = 80.0                   !   [km]</span>
<span id="L248">                                ! The latitudinal or y-direction length of the domain.</span>
<span id="L249">WESTLON = 320.0                 !   [km] default = 0.0</span>
<span id="L250">                                ! The western longitude of the domain or the equivalent starting value for the</span>
<span id="L251">                                ! x-axis.</span>
<span id="L252">LENLON = 480.0                  !   [km]</span>
<span id="L253">                                ! The longitudinal or x-direction length of the domain.</span>
<span id="L254">RAD_EARTH = 6.378E+06           !   [m] default = 6.378E+06</span>
<span id="L255">                                ! The radius of the Earth.</span>
<span id="L256">TOPO_CONFIG = &quot;ISOMIP&quot;          !</span>
<span id="L257">                                ! This specifies how bathymetry is specified:</span>
<span id="L258">                                !     file - read bathymetric information from the file</span>
<span id="L259">                                !       specified by (TOPO_FILE).</span>
<span id="L260">                                !     flat - flat bottom set to MAXIMUM_DEPTH.</span>
<span id="L261">                                !     bowl - an analytically specified bowl-shaped basin</span>
<span id="L262">                                !       ranging between MAXIMUM_DEPTH and MINIMUM_DEPTH.</span>
<span id="L263">                                !     spoon - a similar shape to &#x27;bowl&#x27;, but with an vertical</span>
<span id="L264">                                !       wall at the southern face.</span>
<span id="L265">                                !     halfpipe - a zonally uniform channel with a half-sine</span>
<span id="L266">                                !       profile in the meridional direction.</span>
<span id="L267">                                !     bbuilder - build topography from list of functions.</span>
<span id="L268">                                !     benchmark - use the benchmark test case topography.</span>
<span id="L269">                                !     Neverworld - use the Neverworld test case topography.</span>
<span id="L270">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L271">                                !       DOME sill-overflow test case.</span>
<span id="L272">                                !     ISOMIP - use a slope and channel configuration for the</span>
<span id="L273">                                !       ISOMIP test case.</span>
<span id="L274">                                !     DOME2D - use a shelf and slope configuration for the</span>
<span id="L275">                                !       DOME2D gravity current/overflow test case.</span>
<span id="L276">                                !     Kelvin - flat but with rotated land mask.</span>
<span id="L277">                                !     seamount - Gaussian bump for spontaneous motion test case.</span>
<span id="L278">                                !     dumbbell - Sloshing channel with reservoirs on both ends.</span>
<span id="L279">                                !     shelfwave - exponential slope for shelfwave test case.</span>
<span id="L280">                                !     Phillips - ACC-like idealized topography used in the Phillips config.</span>
<span id="L281">                                !     dense - Denmark Strait-like dense water formation and overflow.</span>
<span id="L282">                                !     USER - call a user modified routine.</span>
<span id="L283"></span>
<span id="L284">! === module ISOMIP_initialize_topography ===</span>
<span id="L285">MINIMUM_DEPTH = 1.0             !   [m] default = 0.0</span>
<span id="L286">                                ! The minimum depth of the ocean.</span>
<span id="L287">ISOMIP_2D = False               !   [Boolean] default = False</span>
<span id="L288">                                ! If true, use a 2D setup.</span>
<span id="L289">ISOMIP_MAX_BEDROCK = 720.0      !   [m] default = 720.0</span>
<span id="L290">                                ! Maximum depth of bedrock topography in the ISOMIP configuration.</span>
<span id="L291">ISOMIP_TROUGH_DEPTH = 500.0     !   [m] default = 500.0</span>
<span id="L292">                                ! Depth of the trough compared with side walls in the ISOMIP configuration.</span>
<span id="L293">ISOMIP_BEDROCK_LENGTH = 3.0E+05 !   [m] default = 3.0E+05</span>
<span id="L294">                                ! Characteristic along-flow length scale of the bedrock in the ISOMIP</span>
<span id="L295">                                ! configuration.</span>
<span id="L296">ISOMIP_TROUGH_WIDTH = 2.4E+04   !   [m] default = 2.4E+04</span>
<span id="L297">                                ! Half-width of the trough in the ISOMIP configuration.</span>
<span id="L298">ISOMIP_DOMAIN_WIDTH = 8.0E+04   !   [m] default = 8.0E+04</span>
<span id="L299">                                ! Domain width (across ice flow) in the ISOMIP configuration.</span>
<span id="L300">ISOMIP_SIDE_WIDTH = 4000.0      !   [m] default = 4000.0</span>
<span id="L301">                                ! Characteristic width of the side walls of the channel in the ISOMIP</span>
<span id="L302">                                ! configuration.</span>
<span id="L303">MAXIMUM_DEPTH = 720.0           !   [m]</span>
<span id="L304">                                ! The maximum depth of the ocean.</span>
<span id="L305"></span>
<span id="L306">! === module MOM_open_boundary ===</span>
<span id="L307">! Controls where open boundaries are located, what kind of boundary condition to impose, and what data to apply,</span>
<span id="L308">! if any.</span>
<span id="L309">OBC_NUMBER_OF_SEGMENTS = 0      ! default = 0</span>
<span id="L310">                                ! The number of open boundary segments.</span>
<span id="L311">MASKING_DEPTH = -9999.0         !   [m] default = -9999.0</span>
<span id="L312">                                ! The depth below which to mask points as land points, for which all fluxes are</span>
<span id="L313">                                ! zeroed out. MASKING_DEPTH is ignored if it has the special default value.</span>
<span id="L314">CHANNEL_CONFIG = &quot;none&quot;         ! default = &quot;none&quot;</span>
<span id="L315">                                ! A parameter that determines which set of channels are</span>
<span id="L316">                                ! restricted to specific  widths.  Options are:</span>
<span id="L317">                                !     none - All channels have the grid width.</span>
<span id="L318">                                !     global_1deg - Sets 16 specific channels appropriate</span>
<span id="L319">                                !       for a 1-degree model, as used in CM2G.</span>
<span id="L320">                                !     list - Read the channel locations and widths from a</span>
<span id="L321">                                !       text file, like MOM_channel_list in the MOM_SIS</span>
<span id="L322">                                !       test case.</span>
<span id="L323">                                !     file - Read open face widths everywhere from a</span>
<span id="L324">                                !       NetCDF file on the model grid.</span>
<span id="L325">SUBGRID_TOPO_AT_VEL = False     !   [Boolean] default = False</span>
<span id="L326">                                ! If true, use variables from TOPO_AT_VEL_FILE as parameters for porous barrier.</span>
<span id="L327">ROTATION = &quot;beta&quot;               ! default = &quot;2omegasinlat&quot;</span>
<span id="L328">                                ! This specifies how the Coriolis parameter is specified:</span>
<span id="L329">                                !     2omegasinlat - Use twice the planetary rotation rate</span>
<span id="L330">                                !       times the sine of latitude.</span>
<span id="L331">                                !     betaplane - Use a beta-plane or f-plane.</span>
<span id="L332">                                !     USER - call a user modified routine.</span>
<span id="L333">F_0 = -1.408706225059977E-04    !   [s-1] default = 0.0</span>
<span id="L334">                                ! The reference value of the Coriolis parameter with the betaplane option.</span>
<span id="L335">BETA = 0.0                      !   [m-1 s-1] default = 0.0</span>
<span id="L336">                                ! The northward gradient of the Coriolis parameter with the betaplane option.</span>
<span id="L337">BETA_LAT_REF = 0.0              !   [kilometers] default = 0.0</span>
<span id="L338">                                ! The reference latitude (origin) of the beta-plane</span>
<span id="L339">GRID_ROTATION_ANGLE_BUGS = False !   [Boolean] default = False</span>
<span id="L340">                                ! If true, use an older algorithm to calculate the sine and cosines needed</span>
<span id="L341">                                ! rotate between grid-oriented directions and true north and east.  Differences</span>
<span id="L342">                                ! arise at the tripolar fold.</span>
<span id="L343"></span>
<span id="L344">! === module MOM_verticalGrid ===</span>
<span id="L345">! Parameters providing information about the vertical grid.</span>
<span id="L346">G_EARTH = 9.8                   !   [m s-2] default = 9.8</span>
<span id="L347">                                ! The gravitational acceleration of the Earth.</span>
<span id="L348">RHO_0 = 1027.0                  !   [kg m-3] default = 1035.0</span>
<span id="L349">                                ! The mean ocean density used with BOUSSINESQ true to calculate accelerations</span>
<span id="L350">                                ! and the mass for conservation properties, or with BOUSSINSEQ false to convert</span>
<span id="L351">                                ! some parameters from vertical units of m to kg m-2.</span>
<span id="L352">BOUSSINESQ = True               !   [Boolean] default = True</span>
<span id="L353">                                ! If true, make the Boussinesq approximation.</span>
<span id="L354">ANGSTROM = 1.0E-15              !   [m] default = 1.0E-10</span>
<span id="L355">                                ! The minimum layer thickness, usually one-Angstrom.</span>
<span id="L356">H_TO_M = 1.0                    !   [m H-1] default = 1.0</span>
<span id="L357">                                ! A constant that translates the model&#x27;s internal units of thickness into m.</span>
<span id="L358">NK = 36                         !   [nondim]</span>
<span id="L359">                                ! The number of model layers.</span>
<span id="L360">ADVECTION_SCHEME_VARIANCE_UNDERFLOW = 1.0E-23 !   [Conc2 (tracer dependent)] default = 1.0E-23</span>
<span id="L361">                                ! A tiny magnitude for variance used to determine when advection scheme variance</span>
<span id="L362">                                ! production is set to 0.</span>
<span id="L363"></span>
<span id="L364">! === module MOM_tracer_registry ===</span>
<span id="L365"></span>
<span id="L366">! === module MOM_EOS ===</span>
<span id="L367">EQN_OF_STATE = &quot;LINEAR&quot;         ! default = &quot;WRIGHT_FULL&quot;</span>
<span id="L368">                                ! EQN_OF_STATE determines which ocean equation of state should be used.</span>
<span id="L369">                                ! Currently, the valid choices are &quot;LINEAR&quot;, &quot;UNESCO&quot;, &quot;JACKETT_MCD&quot;, &quot;WRIGHT&quot;,</span>
<span id="L370">                                ! &quot;WRIGHT_REDUCED&quot;, &quot;WRIGHT_FULL&quot;, &quot;NEMO&quot;, &quot;ROQUET_RHO&quot;, &quot;ROQUET_SPV&quot; and</span>
<span id="L371">                                ! &quot;TEOS10&quot;.  This is only used if USE_EOS is true.</span>
<span id="L372">RHO_REF_LINEAR_EOS = 1000.0     !   [kg m-3] default = 1000.0</span>
<span id="L373">                                ! When EQN_OF_STATE=LINEAR, this is the density at T=T_REF_LINEAR_EOS,</span>
<span id="L374">                                ! S=S_REF_LINEAR_EOS and p=P_REF_LINEAR_EOS</span>
<span id="L375">T_REF_LINEAR_EOS = 0.0          !   [degC] default = 0.0</span>
<span id="L376">                                ! When EQN_OF_STATE=LINEAR, this is the reference temperature.</span>
<span id="L377">S_REF_LINEAR_EOS = 0.0          !   [psu] default = 0.0</span>
<span id="L378">                                ! When EQN_OF_STATE=LINEAR, this is the reference salinity.</span>
<span id="L379">P_REF_LINEAR_EOS = 0.0          !   [Pa] default = 0.0</span>
<span id="L380">                                ! When EQN_OF_STATE=LINEAR, this is the reference pressure.</span>
<span id="L381">DRHO_DT = -0.0383569483         !   [kg m-3 K-1] default = -0.2</span>
<span id="L382">                                ! When EQN_OF_STATE=LINEAR, this is the partial derivative of density with</span>
<span id="L383">                                ! temperature.</span>
<span id="L384">DRHO_DS = 0.805876093           !   [kg m-3 ppt-1] default = 0.8</span>
<span id="L385">                                ! When EQN_OF_STATE=LINEAR, this is the partial derivative of density with</span>
<span id="L386">                                ! salinity.</span>
<span id="L387">DRHO_DP = 0.0                   !   [s2 m-2] default = 0.0</span>
<span id="L388">                                ! When EQN_OF_STATE=LINEAR, this is the partial derivative of density with</span>
<span id="L389">                                ! pressure (the inverse of sound speed squared).</span>
<span id="L390">RHO_T0_S0 = 999.9106806711001   !   [kg m-3] default = 1000.0</span>
<span id="L391">                                ! When EQN_OF_STATE=LINEAR, this is the density at T=0, S=0 and p=0.  If</span>
<span id="L392">                                ! RHO_TO_SO is specified, RHO_REF_LINEAR_EOS, T_REF_LINEAR_EOS, S_REF_LINEAR_EOS</span>
<span id="L393">                                ! and P_REF_LINEAR_EOS are not used.</span>
<span id="L394">EOS_QUADRATURE = False          !   [Boolean] default = False</span>
<span id="L395">                                ! If true, always use the generic (quadrature) code code for the integrals of</span>
<span id="L396">                                ! density.</span>
<span id="L397">TFREEZE_FORM = &quot;LINEAR&quot;         ! default = &quot;LINEAR&quot;</span>
<span id="L398">                                ! TFREEZE_FORM determines which expression should be used for the freezing</span>
<span id="L399">                                ! point.  Currently, the valid choices are &quot;LINEAR&quot;, &quot;MILLERO_78&quot;, &quot;TEOS_POLY&quot;,</span>
<span id="L400">                                ! &quot;TEOS10&quot;</span>
<span id="L401">TFREEZE_S0_P0 = 0.0832          !   [degC] default = 0.0</span>
<span id="L402">                                ! When TFREEZE_FORM=LINEAR, this is the freezing potential temperature at S=0,</span>
<span id="L403">                                ! P=0.</span>
<span id="L404">DTFREEZE_DS = -0.0573           !   [degC ppt-1] default = -0.054</span>
<span id="L405">                                ! When TFREEZE_FORM=LINEAR, this is the derivative of the freezing potential</span>
<span id="L406">                                ! temperature with salinity.</span>
<span id="L407">DTFREEZE_DP = -7.53E-08         !   [degC Pa-1] default = 0.0</span>
<span id="L408">                                ! When TFREEZE_FORM=LINEAR, this is the derivative of the freezing potential</span>
<span id="L409">                                ! temperature with pressure.</span>
<span id="L410">TFREEZE_S_IS_PRACS = True       !   [Boolean] default = True</span>
<span id="L411">                                ! When True, the model will check if the model internal salinity is practical</span>
<span id="L412">                                ! salinity.  If the model uses absolute salinity, a conversion will be applied.</span>
<span id="L413">TFREEZE_T_IS_POTT = True        !   [Boolean] default = True</span>
<span id="L414">                                ! When True, the model will check if the model internal temperature is potential</span>
<span id="L415">                                ! temperature.  If the model uses conservative temperature, a conversion will be</span>
<span id="L416">                                ! applied.</span>
<span id="L417"></span>
<span id="L418">! === module MOM_restart ===</span>
<span id="L419">PARALLEL_RESTARTFILES = False   !   [Boolean] default = False</span>
<span id="L420">                                ! If true, the IO layout is used to group processors that write to the same</span>
<span id="L421">                                ! restart file or each processor writes its own (numbered) restart file. If</span>
<span id="L422">                                ! false, a single restart file is generated combining output from all PEs.</span>
<span id="L423">RESTARTFILE = &quot;MOM.res&quot;         ! default = &quot;MOM.res&quot;</span>
<span id="L424">                                ! The name-root of the restart file.</span>
<span id="L425">MAX_FIELDS = 100                ! default = 100</span>
<span id="L426">                                ! The maximum number of restart fields that can be used.</span>
<span id="L427">RESTART_CHECKSUMS_REQUIRED = True !   [Boolean] default = True</span>
<span id="L428">                                ! If true, require the restart checksums to match and error out otherwise. Users</span>
<span id="L429">                                ! may want to avoid this comparison if for example the restarts are made from a</span>
<span id="L430">                                ! run with a different mask_table than the current run, in which case the</span>
<span id="L431">                                ! checksums will not match and cause crash.</span>
<span id="L432">RESTART_SYMMETRIC_CHECKSUMS = False !   [Boolean] default = False</span>
<span id="L433">                                ! If true, do the restart checksums on all the edge points for a non-reentrant</span>
<span id="L434">                                ! grid.  This requires that SYMMETRIC_MEMORY_ is defined at compile time.</span>
<span id="L435">RESTART_UNSIGNED_ZEROS = False  !   [Boolean] default = False</span>
<span id="L436">                                ! If true, convert any negative zeros that would be written to the restart file</span>
<span id="L437">                                ! into ordinary unsigned zeros.  This does not change answers, but it can be</span>
<span id="L438">                                ! helpful in comparing restart files after grid rotation, for example.</span>
<span id="L439">USE_FILTER = False              !   [Boolean] default = False</span>
<span id="L440">                                ! If true, use streaming band-pass filters to detect the instantaneous tidal</span>
<span id="L441">                                ! signals in the simulation.</span>
<span id="L442"></span>
<span id="L443">! === module MOM_tracer_flow_control ===</span>
<span id="L444">USE_USER_TRACER_EXAMPLE = False !   [Boolean] default = False</span>
<span id="L445">                                ! If true, use the USER_tracer_example tracer package.</span>
<span id="L446">USE_DOME_TRACER = False         !   [Boolean] default = False</span>
<span id="L447">                                ! If true, use the DOME_tracer tracer package.</span>
<span id="L448">USE_ISOMIP_TRACER = False       !   [Boolean] default = False</span>
<span id="L449">                                ! If true, use the ISOMIP_tracer tracer package.</span>
<span id="L450">USE_RGC_TRACER = False          !   [Boolean] default = False</span>
<span id="L451">                                ! If true, use the RGC_tracer tracer package.</span>
<span id="L452">USE_IDEAL_AGE_TRACER = False    !   [Boolean] default = False</span>
<span id="L453">                                ! If true, use the ideal_age_example tracer package.</span>
<span id="L454">USE_MARBL_TRACERS = False       !   [Boolean] default = False</span>
<span id="L455">                                ! If true, use the MARBL tracer package.</span>
<span id="L456">USE_REGIONAL_DYES = False       !   [Boolean] default = False</span>
<span id="L457">                                ! If true, use the regional_dyes tracer package.</span>
<span id="L458">USE_FILE_DYES = False           !   [Boolean] default = False</span>
<span id="L459">                                ! If true, use the file dyes tracer package.</span>
<span id="L460">USE_OIL_TRACER = False          !   [Boolean] default = False</span>
<span id="L461">                                ! If true, use the oil_tracer tracer package.</span>
<span id="L462">USE_ADVECTION_TEST_TRACER = False !   [Boolean] default = False</span>
<span id="L463">                                ! If true, use the advection_test_tracer tracer package.</span>
<span id="L464">USE_OCMIP2_CFC = False          !   [Boolean] default = False</span>
<span id="L465">                                ! If true, use the MOM_OCMIP2_CFC tracer package.</span>
<span id="L466">USE_CFC_CAP = False             !   [Boolean] default = False</span>
<span id="L467">                                ! If true, use the MOM_CFC_cap tracer package.</span>
<span id="L468">USE_generic_tracer = False      !   [Boolean] default = False</span>
<span id="L469">                                ! If true and _USE_GENERIC_TRACER is defined as a preprocessor macro, use the</span>
<span id="L470">                                ! MOM_generic_tracer packages.</span>
<span id="L471">USE_PSEUDO_SALT_TRACER = False  !   [Boolean] default = False</span>
<span id="L472">                                ! If true, use the pseudo salt tracer, typically run as a diagnostic.</span>
<span id="L473">USE_BOUNDARY_IMPULSE_TRACER = False !   [Boolean] default = False</span>
<span id="L474">                                ! If true, use the boundary impulse tracer.</span>
<span id="L475">USE_DYED_OBC_TRACER = False     !   [Boolean] default = False</span>
<span id="L476">                                ! If true, use the dyed_obc_tracer tracer package.</span>
<span id="L477">USE_NW2_TRACERS = False         !   [Boolean] default = False</span>
<span id="L478">                                ! If true, use the NeverWorld2 tracers.</span>
<span id="L479"></span>
<span id="L480">! === module MOM_coord_initialization ===</span>
<span id="L481">COORD_CONFIG = &quot;linear&quot;         ! default = &quot;none&quot;</span>
<span id="L482">                                ! This specifies how layers are to be defined:</span>
<span id="L483">                                !     ALE or none - used to avoid defining layers in ALE mode</span>
<span id="L484">                                !     file - read coordinate information from the file</span>
<span id="L485">                                !       specified by (COORD_FILE).</span>
<span id="L486">                                !     BFB - Custom coords for buoyancy-forced basin case</span>
<span id="L487">                                !       based on SST_S, T_BOT and DRHO_DT.</span>
<span id="L488">                                !     linear - linear based on interfaces not layers</span>
<span id="L489">                                !     layer_ref - linear based on layer densities</span>
<span id="L490">                                !     ts_ref - use reference temperature and salinity</span>
<span id="L491">                                !     ts_range - use range of temperature and salinity</span>
<span id="L492">                                !       (T_REF and S_REF) to determine surface density</span>
<span id="L493">                                !       and GINT calculate internal densities.</span>
<span id="L494">                                !     gprime - use reference density (RHO_0) for surface</span>
<span id="L495">                                !       density and GINT calculate internal densities.</span>
<span id="L496">                                !     ts_profile - use temperature and salinity profiles</span>
<span id="L497">                                !       (read from COORD_FILE) to set layer densities.</span>
<span id="L498">                                !     USER - call a user modified routine.</span>
<span id="L499">LIGHTEST_DENSITY = 1027.1524    !   [kg m-3] default = 1027.0</span>
<span id="L500">                                ! The reference potential density used for the surface interface.</span>
<span id="L501">DENSITY_RANGE = 0.7438856       !   [kg m-3] default = 2.0</span>
<span id="L502">                                ! The range of reference potential densities across all interfaces.</span>
<span id="L503">GFS = 9.8                       !   [m s-2] default = 9.8</span>
<span id="L504">                                ! The reduced gravity at the free surface.</span>
<span id="L505">REGRIDDING_COORDINATE_MODE = &quot;SIGMA_SHELF_ZSTAR&quot; ! default = &quot;LAYER&quot;</span>
<span id="L506">                                ! Coordinate mode for vertical regridding. Choose among the following</span>
<span id="L507">                                ! possibilities:  LAYER - Isopycnal or stacked shallow water layers</span>
<span id="L508">                                !  ZSTAR, Z* - stretched geopotential z*</span>
<span id="L509">                                !  SIGMA_SHELF_ZSTAR - stretched geopotential z* ignoring shelf</span>
<span id="L510">                                !  SIGMA - terrain following coordinates</span>
<span id="L511">                                !  RHO   - continuous isopycnal</span>
<span id="L512">                                !  HYCOM1 - HyCOM-like hybrid coordinate</span>
<span id="L513">                                !  HYBGEN - Hybrid coordinate from the Hycom hybgen code</span>
<span id="L514">                                !  ADAPTIVE - optimize for smooth neutral density surfaces</span>
<span id="L515">REGRIDDING_COORDINATE_UNITS = &quot;m&quot; ! default = &quot;m&quot;</span>
<span id="L516">                                ! Units of the regridding coordinate.</span>
<span id="L517">ALE_COORDINATE_CONFIG = &quot;UNIFORM&quot; ! default = &quot;UNIFORM&quot;</span>
<span id="L518">                                ! Determines how to specify the coordinate resolution. Valid options are:</span>
<span id="L519">                                !  PARAM       - use the vector-parameter ALE_RESOLUTION</span>
<span id="L520">                                !  UNIFORM[:N] - uniformly distributed</span>
<span id="L521">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L522">                                !                the filename and variable name, separated</span>
<span id="L523">                                !                by a comma or space, e.g. FILE:lev.nc,dz</span>
<span id="L524">                                !                or FILE:lev.nc,interfaces=zw</span>
<span id="L525">                                !  WOA09[:N]   - the WOA09 vertical grid (approximately)</span>
<span id="L526">                                !  WOA09INT[:N] - layers spanned by the WOA09 depths</span>
<span id="L527">                                !  WOA23INT[:N] - layers spanned by the WOA23 depths</span>
<span id="L528">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L529">                                !  HYBRID:string - read from a file. The string specifies</span>
<span id="L530">                                !                the filename and two variable names, separated</span>
<span id="L531">                                !                by a comma or space, for sigma-2 and dz.</span>
<span id="L532">                                !                e.g. HYBRID:vgrid.nc,sigma2,dz</span>
<span id="L533">                                !  HYBRID_3D:string - read from a file. The string specifies</span>
<span id="L534">                                !                the filename and two 3D variable names, separated</span>
<span id="L535">                                !                by a comma or space, for sigma-2 and dz. The</span>
<span id="L536">                                !                latter can be FNC1:string which is used everywhere.</span>
<span id="L537">                                !                e.g. HYBRID_3D:vgrid.nc,sigma2,dz</span>
<span id="L538">                                !  HYBRID_MAP:string - read from a file. The string specifies</span>
<span id="L539">                                !                the filename and three variable names, separated</span>
<span id="L540">                                !                by a comma or space, for map, sigma-2 and dz.</span>
<span id="L541">                                !                Map is a spatial index array with, maxval(map)=N,</span>
<span id="L542">                                !                and the others are 2D arrays containing N profiles.</span>
<span id="L543">                                !                Map typically contains integer values, but it can</span>
<span id="L544">                                !                contain real values, I+w, which imply using</span>
<span id="L545">                                !                the weighted sum of profiles I and I+1.</span>
<span id="L546">                                !                Dz can be FNC1:string which is used everywhere.</span>
<span id="L547">                                !                e.g. HYBRID_MAP:vgrid.nc,map,sigma2,dz</span>
<span id="L548">!ALE_RESOLUTION = 36*20.0       !   [m]</span>
<span id="L549">                                ! The distribution of vertical resolution for the target</span>
<span id="L550">                                ! grid used for Eulerian-like coordinates. For example,</span>
<span id="L551">                                ! in z-coordinate mode, the parameter is a list of level</span>
<span id="L552">                                ! thicknesses (in m). In sigma-coordinate mode, the list</span>
<span id="L553">                                ! is of non-dimensional fractions of the water column.</span>
<span id="L554">MIN_THICKNESS = 1.0E-12         !   [m] default = 0.001</span>
<span id="L555">                                ! When regridding, this is the minimum layer thickness allowed.</span>
<span id="L556">REMAPPING_SCHEME = &quot;PPM_H4&quot;     ! default = &quot;PLM&quot;</span>
<span id="L557">                                ! This sets the reconstruction scheme used for vertical remapping for all</span>
<span id="L558">                                ! variables. It can be one of the following schemes:</span>
<span id="L559">                                ! PCM         (1st-order accurate)</span>
<span id="L560">                                ! PLM         (2nd-order accurate)</span>
<span id="L561">                                ! PLM_HYBGEN  (2nd-order accurate)</span>
<span id="L562">                                ! PPM_H4      (3rd-order accurate)</span>
<span id="L563">                                ! PPM_IH4     (3rd-order accurate)</span>
<span id="L564">                                ! PPM_HYBGEN  (3rd-order accurate)</span>
<span id="L565">                                ! WENO_HYBGEN (3rd-order accurate)</span>
<span id="L566">                                ! PQM_IH4IH3  (4th-order accurate)</span>
<span id="L567">                                ! PQM_IH6IH5  (5th-order accurate)</span>
<span id="L568">VELOCITY_REMAPPING_SCHEME = &quot;PPM_H4&quot; ! default = &quot;PPM_H4&quot;</span>
<span id="L569">                                ! This sets the reconstruction scheme used for vertical remapping of velocities.</span>
<span id="L570">                                ! By default it is the same as REMAPPING_SCHEME. It can be one of the following</span>
<span id="L571">                                ! schemes:</span>
<span id="L572">                                ! PCM         (1st-order accurate)</span>
<span id="L573">                                ! PLM         (2nd-order accurate)</span>
<span id="L574">                                ! PLM_HYBGEN  (2nd-order accurate)</span>
<span id="L575">                                ! PPM_H4      (3rd-order accurate)</span>
<span id="L576">                                ! PPM_IH4     (3rd-order accurate)</span>
<span id="L577">                                ! PPM_HYBGEN  (3rd-order accurate)</span>
<span id="L578">                                ! WENO_HYBGEN (3rd-order accurate)</span>
<span id="L579">                                ! PQM_IH4IH3  (4th-order accurate)</span>
<span id="L580">                                ! PQM_IH6IH5  (5th-order accurate)</span>
<span id="L581">FATAL_CHECK_RECONSTRUCTIONS = False !   [Boolean] default = False</span>
<span id="L582">                                ! If true, cell-by-cell reconstructions are checked for consistency and if</span>
<span id="L583">                                ! non-monotonicity or an inconsistency is detected then a FATAL error is issued.</span>
<span id="L584">FATAL_CHECK_REMAPPING = False   !   [Boolean] default = False</span>
<span id="L585">                                ! If true, the results of remapping are checked for conservation and new extrema</span>
<span id="L586">                                ! and if an inconsistency is detected then a FATAL error is issued.</span>
<span id="L587">REMAP_BOUND_INTERMEDIATE_VALUES = False !   [Boolean] default = False</span>
<span id="L588">                                ! If true, the values on the intermediate grid used for remapping are forced to</span>
<span id="L589">                                ! be bounded, which might not be the case due to round off.</span>
<span id="L590">REMAP_BOUNDARY_EXTRAP = False   !   [Boolean] default = False</span>
<span id="L591">                                ! If true, values at the interfaces of boundary cells are extrapolated instead</span>
<span id="L592">                                ! of piecewise constant</span>
<span id="L593">INIT_BOUNDARY_EXTRAP = True     !   [Boolean] default = False</span>
<span id="L594">                                ! If true, values at the interfaces of boundary cells are extrapolated instead</span>
<span id="L595">                                ! of piecewise constant during initialization.Defaults to REMAP_BOUNDARY_EXTRAP.</span>
<span id="L596">REMAPPING_USE_OM4_SUBCELLS = False !   [Boolean] default = True</span>
<span id="L597">                                ! This selects the remapping algorithm used in OM4 that does not use the full</span>
<span id="L598">                                ! reconstruction for the top- and lower-most sub-layers, but instead assumes</span>
<span id="L599">                                ! they are always vanished (untrue) and so just uses their edge values. We</span>
<span id="L600">                                ! recommend setting this option to false.</span>
<span id="L601">REMAPPING_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L602">                                ! The vintage of the expressions and order of arithmetic to use for remapping.</span>
<span id="L603">                                ! Values below 20190101 result in the use of older, less accurate expressions</span>
<span id="L604">                                ! that were in use at the end of 2018.  Higher values result in the use of more</span>
<span id="L605">                                ! robust and accurate forms of mathematically equivalent expressions.</span>
<span id="L606">PARTIAL_CELL_VELOCITY_REMAP = False !   [Boolean] default = False</span>
<span id="L607">                                ! If true, use partial cell thicknesses at velocity points that are masked out</span>
<span id="L608">                                ! where they extend below the shallower of the neighboring bathymetry for</span>
<span id="L609">                                ! remapping velocity.</span>
<span id="L610">REMAP_AFTER_INITIALIZATION = True !   [Boolean] default = True</span>
<span id="L611">                                ! If true, applies regridding and remapping immediately after initialization so</span>
<span id="L612">                                ! that the state is ALE consistent. This is a legacy step and should not be</span>
<span id="L613">                                ! needed if the initialization is consistent with the coordinate mode.</span>
<span id="L614">REGRID_TIME_SCALE = 0.0         !   [s] default = 0.0</span>
<span id="L615">                                ! The time-scale used in blending between the current (old) grid and the target</span>
<span id="L616">                                ! (new) grid. A short time-scale favors the target grid (0. or anything less</span>
<span id="L617">                                ! than DT_THERM) has no memory of the old grid. A very long time-scale makes the</span>
<span id="L618">                                ! model more Lagrangian.</span>
<span id="L619">REGRID_FILTER_SHALLOW_DEPTH = 0.0 !   [m] default = 0.0</span>
<span id="L620">                                ! The depth above which no time-filtering is applied. Above this depth final</span>
<span id="L621">                                ! grid exactly matches the target (new) grid.</span>
<span id="L622">REGRID_FILTER_DEEP_DEPTH = 0.0  !   [m] default = 0.0</span>
<span id="L623">                                ! The depth below which full time-filtering is applied with time-scale</span>
<span id="L624">                                ! REGRID_TIME_SCALE. Between depths REGRID_FILTER_SHALLOW_DEPTH and</span>
<span id="L625">                                ! REGRID_FILTER_SHALLOW_DEPTH the filter weights adopt a cubic profile.</span>
<span id="L626">REMAP_VEL_MASK_BBL_THICK = -0.001 !   [m] default = -0.001</span>
<span id="L627">                                ! A thickness of a bottom boundary layer below which velocities in thin layers</span>
<span id="L628">                                ! are zeroed out after remapping, following practice with Hybgen remapping, or a</span>
<span id="L629">                                ! negative value to avoid such filtering altogether.</span>
<span id="L630">REMAP_VEL_CONSERVE_KE = False   !   [Boolean] default = False</span>
<span id="L631">                                ! If true, a correction is applied to the baroclinic component of velocity after</span>
<span id="L632">                                ! remapping so that total KE is conserved. KE may not be conserved when</span>
<span id="L633">                                ! (CS%BBL_h_vel_mask &gt; 0.0) .and. (CS%h_vel_mask &gt; 0.0)</span>
<span id="L634"></span>
<span id="L635">! === module MOM_domains min_halo ===</span>
<span id="L636"></span>
<span id="L637">! === module MOM_grid ===</span>
<span id="L638">! Parameters providing information about the lateral grid.</span>
<span id="L639"></span>
<span id="L640">! === module MOM_hor_index ===</span>
<span id="L641">! Sets the horizontal array index types.</span>
<span id="L642"></span>
<span id="L643">! === module MOM_grid_init ===</span>
<span id="L644"></span>
<span id="L645">! === module ISOMIP_initialize_topography ===</span>
<span id="L646">MOM_ICESHELF_AVAILABLE_DIAGS_FILE = &quot;MOM_IceShelf.available_diags&quot; ! default = &quot;MOM_IceShelf.available_diags&quot;</span>
<span id="L647">                                ! A file into which to write a list of all available ice shelf diagnostics that</span>
<span id="L648">                                ! can be included in a diag_table.</span>
<span id="L649"></span>
<span id="L650">! === module MOM_ice_shelf ===</span>
<span id="L651">DEBUG_IS = False                !   [Boolean] default = False</span>
<span id="L652">                                ! If true, write verbose debugging messages for the ice shelf.</span>
<span id="L653">DYNAMIC_SHELF_MASS = False      !   [Boolean] default = False</span>
<span id="L654">                                ! If true, the ice sheet mass can evolve with time.</span>
<span id="L655">SHELF_THERMO = True             !   [Boolean] default = False</span>
<span id="L656">                                ! If true, use a thermodynamically interactive ice shelf.</span>
<span id="L657">LATENT_HEAT_FUSION = 3.34E+05   !   [J/kg] default = 3.34E+05</span>
<span id="L658">                                ! The latent heat of fusion.</span>
<span id="L659">SHELF_THREE_EQN = True          !   [Boolean] default = True</span>
<span id="L660">                                ! If true, use the three equation expression of consistency to calculate the</span>
<span id="L661">                                ! fluxes at the ice-ocean interface.</span>
<span id="L662">SHELF_INSULATOR = True          !   [Boolean] default = False</span>
<span id="L663">                                ! If true, the ice shelf is a perfect insulator (no conduction).</span>
<span id="L664">MELTING_CUTOFF_DEPTH = 0.0      !   [m] default = 0.0</span>
<span id="L665">                                ! Depth above which the melt is set to zero (it must be &gt;= 0) Default value</span>
<span id="L666">                                ! won&#x27;t affect the solution.</span>
<span id="L667">CONST_SEA_LEVEL = False         !   [Boolean] default = False</span>
<span id="L668">                                ! If true, apply evaporative, heat and salt fluxes in the sponge region. This</span>
<span id="L669">                                ! will avoid a large increase in sea level. This option is needed for some of</span>
<span id="L670">                                ! the ISOMIP+ experiments (Ocean3 and Ocean4). IMPORTANT: it is not currently</span>
<span id="L671">                                ! possible to do prefect restarts using this flag.</span>
<span id="L672">CONST_SEA_LEVEL_MISOMIP = False !   [Boolean] default = False</span>
<span id="L673">                                ! If true, constant_sea_level fluxes are applied only over the surface sponge</span>
<span id="L674">                                ! cells from the ISOMIP/MISOMIP configuration</span>
<span id="L675">SHELF_3EQ_GAMMA = False         !   [Boolean] default = False</span>
<span id="L676">                                ! If true, user specifies a constant nondimensional heat-transfer coefficient</span>
<span id="L677">                                ! (GAMMA_T_3EQ), from which the default salt-transfer coefficient is set as</span>
<span id="L678">                                ! GAMMA_T_3EQ/35. This is used with SHELF_THREE_EQN.</span>
<span id="L679">SHELF_S_ROOT = False            !   [Boolean] default = False</span>
<span id="L680">                                ! If SHELF_S_ROOT = True, salinity at the ice/ocean interface (Sbdry) is</span>
<span id="L681">                                ! computed from a quadratic equation. Otherwise, the previous interactive method</span>
<span id="L682">                                ! to estimate Sbdry is used.</span>
<span id="L683">ICE_SHELF_MASS_FROM_FILE = False !   [Boolean] default = False</span>
<span id="L684">                                ! Read the mass of the ice shelf (every time step) from a file.</span>
<span id="L685">C_P_ICE = 2100.0                !   [J kg-1 K-1] default = 2100.0</span>
<span id="L686">                                ! The heat capacity of ice.</span>
<span id="L687">ICE_SHELF_FLUX_FACTOR = 1.0     !   [none] default = 1.0</span>
<span id="L688">                                ! Non-dimensional factor applied to shelf thermodynamic fluxes.</span>
<span id="L689">KV_ICE = 1.0E+10                !   [m2 s-1] default = 1.0E+10</span>
<span id="L690">                                ! The viscosity of the ice.</span>
<span id="L691">KV_MOLECULAR = 1.95E-06         !   [m2 s-1] default = 1.95E-06</span>
<span id="L692">                                ! The molecular kinematic viscosity of sea water at the freezing temperature.</span>
<span id="L693">ICE_SHELF_SALINITY = 0.0        !   [psu] default = 0.0</span>
<span id="L694">                                ! The salinity of the ice inside the ice shelf.</span>
<span id="L695">ICE_SHELF_TEMPERATURE = -20.0   !   [degC] default = -15.0</span>
<span id="L696">                                ! The temperature at the center of the ice shelf.</span>
<span id="L697">KD_SALT_MOLECULAR = 8.02E-10    !   [m2 s-1] default = 8.02E-10</span>
<span id="L698">                                ! The molecular diffusivity of salt in sea water at the freezing point.</span>
<span id="L699">KD_TEMP_MOLECULAR = 1.41E-07    !   [m2 s-1] default = 1.41E-07</span>
<span id="L700">                                ! The molecular diffusivity of heat in sea water at the freezing point.</span>
<span id="L701">DT_FORCING = 720.0              !   [s] default = 0.0</span>
<span id="L702">                                ! The time step for changing forcing, coupling with other components, or</span>
<span id="L703">                                ! potentially writing certain diagnostics. The default value is given by DT.</span>
<span id="L704">COL_THICK_MELT_THRESHOLD = 10.0 !   [m] default = 0.0</span>
<span id="L705">                                ! The minimum ocean column thickness where melting is allowed.</span>
<span id="L706">READ_TIDEAMP = False            !   [Boolean] default = False</span>
<span id="L707">                                ! If true, read a file (given by TIDEAMP_FILE) containing the tidal amplitude</span>
<span id="L708">                                ! with INT_TIDE_DISSIPATION.</span>
<span id="L709">ICE_SHELF_LINEAR_SHELF_FRAC = 0.13 !   [nondim] default = 0.13</span>
<span id="L710">                                ! Ratio of HJ99 stability constant xi_N (ratio of maximum mixing length to</span>
<span id="L711">                                ! planetary boundary layer depth in neutrally stable conditions) to the von</span>
<span id="L712">                                ! Karman constant</span>
<span id="L713">ICE_SHELF_VK_CNST = 0.4         !   [nondim] default = 0.4</span>
<span id="L714">                                ! Von Karman constant.</span>
<span id="L715">ICE_SHELF_RC = 0.2              !   [nondim] default = 0.2</span>
<span id="L716">                                ! Critical flux Richardson number for ice melt</span>
<span id="L717">ICE_SHELF_BUOYANCY_FLUX_ITT_BUG = True !   [Boolean] default = True</span>
<span id="L718">                                ! Bug fix of buoyancy iteration</span>
<span id="L719">ICE_SHELF_SALT_FLUX_ITT_BUG = True !   [Boolean] default = True</span>
<span id="L720">                                ! Bug fix of salt iteration</span>
<span id="L721">ICE_SHELF_BUOYANCY_FLUX_ITT_THRESHOLD = 1.0E-04 !   [nondim] default = 1.0E-04</span>
<span id="L722">                                ! Convergence criterion of Newton&#x27;s method for ice shelf buoyancy iteration.</span>
<span id="L723">UTIDE = 0.01                    !   [m s-1] default = 0.0</span>
<span id="L724">                                ! The constant tidal amplitude used with INT_TIDE_DISSIPATION.</span>
<span id="L725"></span>
<span id="L726">! === module MOM_EOS ===</span>
<span id="L727">DENSITY_ICE = 900.0             !   [kg m-3] default = 900.0</span>
<span id="L728">                                ! A typical density of ice.</span>
<span id="L729">MIN_THICKNESS_SIMPLE_CALVE = 0.0 !   [m] default = 0.0</span>
<span id="L730">                                ! Min thickness rule for the very simple calving law</span>
<span id="L731">USTAR_SHELF_BG = 0.001          !   [m s-1] default = 0.0</span>
<span id="L732">                                ! The minimum value of ustar under ice shelves.</span>
<span id="L733">CDRAG_SHELF = 0.025             !   [nondim] default = 0.003</span>
<span id="L734">                                ! CDRAG is the drag coefficient relating the magnitude of the velocity field to</span>
<span id="L735">                                ! the surface stress.</span>
<span id="L736">USTAR_SHELF_FROM_VEL = True     !   [Boolean] default = True</span>
<span id="L737">                                ! If true, use the surface velocities to set the friction velocity under ice</span>
<span id="L738">                                ! shelves instead of using the previous values of the stresses.</span>
<span id="L739"></span>
<span id="L740">! === module MOM_restart ===</span>
<span id="L741">ICE_PROFILE_CONFIG = &quot;FILE&quot;     !</span>
<span id="L742">                                ! This specifies how the initial ice profile is specified. Valid values are:</span>
<span id="L743">                                ! CHANNEL, FILE, and USER.</span>
<span id="L744">ICE_THICKNESS_FILE = &quot;Ocean0_3D_Claire.nc&quot; ! default = &quot;ice_shelf_h.nc&quot;</span>
<span id="L745">                                ! The file from which the bathymetry is read.</span>
<span id="L746">LEN_SIDE_STRESS = 0.0           !   [axis_units] default = 0.0</span>
<span id="L747">                                ! position past which shelf sides are stress free.</span>
<span id="L748">ICE_THICKNESS_VARNAME = &quot;thick&quot; ! default = &quot;h_shelf&quot;</span>
<span id="L749">                                ! The name of the thickness variable in ICE_THICKNESS_FILE.</span>
<span id="L750">ICE_AREA_VARNAME = &quot;area&quot;       ! default = &quot;area_shelf_h&quot;</span>
<span id="L751">                                ! The name of the area variable in ICE_THICKNESS_FILE.</span>
<span id="L752">SHELF_IC_OUTPUT_FILE = &quot;MOM_Shelf_IC&quot; ! default = &quot;MOM_Shelf_IC&quot;</span>
<span id="L753">                                ! The name-root of the output file for the ice shelf initial conditions.</span>
<span id="L754"></span>
<span id="L755">! === module MOM_state_initialization ===</span>
<span id="L756">FATAL_INCONSISTENT_RESTART_TIME = False !   [Boolean] default = False</span>
<span id="L757">                                ! If true and a time_in value is provided to MOM_initialize_state, verify that</span>
<span id="L758">                                ! the time read from a restart file is the same as time_in, and issue a fatal</span>
<span id="L759">                                ! error if it is not.  Otherwise, simply set the time to time_in if present.</span>
<span id="L760">INIT_LAYERS_FROM_Z_FILE = False !   [Boolean] default = False</span>
<span id="L761">                                ! If true, initialize the layer thicknesses, temperatures, and salinities from a</span>
<span id="L762">                                ! Z-space file on a latitude-longitude grid.</span>
<span id="L763">THICKNESS_CONFIG = &quot;ISOMIP&quot;     ! default = &quot;uniform&quot;</span>
<span id="L764">                                ! A string that determines how the initial layer thicknesses are specified for a</span>
<span id="L765">                                ! new run:</span>
<span id="L766">                                !     file - read interface heights from the file specified</span>
<span id="L767">                                !       by (THICKNESS_FILE).</span>
<span id="L768">                                !     thickness_file - read thicknesses from the file specified</span>
<span id="L769">                                !       by (THICKNESS_FILE).</span>
<span id="L770">                                !     mass_file - read thicknesses in units of mass per unit area from the file</span>
<span id="L771">                                !       specified by (THICKNESS_FILE).</span>
<span id="L772">                                !     coord - determined by ALE coordinate.</span>
<span id="L773">                                !     uniform - uniform thickness layers evenly distributed</span>
<span id="L774">                                !       between the surface and MAXIMUM_DEPTH.</span>
<span id="L775">                                !     list - read a list of positive interface depths.</span>
<span id="L776">                                !     param - use thicknesses from parameter THICKNESS_INIT_VALUES.</span>
<span id="L777">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L778">                                !       DOME sill-overflow test case.</span>
<span id="L779">                                !     ISOMIP - use a configuration for the</span>
<span id="L780">                                !       ISOMIP test case.</span>
<span id="L781">                                !     benchmark - use the benchmark test case thicknesses.</span>
<span id="L782">                                !     Neverworld - use the Neverworld test case thicknesses.</span>
<span id="L783">                                !     search - search a density profile for the interface</span>
<span id="L784">                                !       densities. This is not yet implemented.</span>
<span id="L785">                                !     circle_obcs - the circle_obcs test case is used.</span>
<span id="L786">                                !     DOME2D - 2D version of DOME initialization.</span>
<span id="L787">                                !     adjustment2d - 2D lock exchange thickness ICs.</span>
<span id="L788">                                !     sloshing - sloshing gravity thickness ICs.</span>
<span id="L789">                                !     seamount - no motion test with seamount ICs.</span>
<span id="L790">                                !     dumbbell - sloshing channel ICs.</span>
<span id="L791">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L792">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L793">                                !     USER - call a user modified routine.</span>
<span id="L794">TS_CONFIG = &quot;ISOMIP&quot;            !</span>
<span id="L795">                                ! A string that determines how the initial temperatures and salinities are</span>
<span id="L796">                                ! specified for a new run:</span>
<span id="L797">                                !     file - read velocities from the file specified</span>
<span id="L798">                                !       by (TS_FILE).</span>
<span id="L799">                                !     fit - find the temperatures that are consistent with</span>
<span id="L800">                                !       the layer densities and salinity S_REF.</span>
<span id="L801">                                !     TS_profile - use temperature and salinity profiles</span>
<span id="L802">                                !       (read from TS_FILE) to set layer densities.</span>
<span id="L803">                                !     benchmark - use the benchmark test case T &amp; S.</span>
<span id="L804">                                !     linear - linear in logical layer space.</span>
<span id="L805">                                !     DOME2D - 2D DOME initialization.</span>
<span id="L806">                                !     ISOMIP - ISOMIP initialization.</span>
<span id="L807">                                !     adjustment2d - 2d lock exchange T/S ICs.</span>
<span id="L808">                                !     sloshing - sloshing mode T/S ICs.</span>
<span id="L809">                                !     seamount - no motion test with seamount ICs.</span>
<span id="L810">                                !     dumbbell - sloshing channel ICs.</span>
<span id="L811">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L812">                                !     SCM_CVMix_tests - used in the SCM CVMix tests.</span>
<span id="L813">                                !     USER - call a user modified routine.</span>
<span id="L814">ISOMIP_T_SUR = -1.9             !   [degC] default = -1.9</span>
<span id="L815">                                ! Temperature at the surface (interface)</span>
<span id="L816">ISOMIP_S_SUR = 33.8             !   [ppt] default = 33.8</span>
<span id="L817">                                ! Salinity at the surface (interface)</span>
<span id="L818">ISOMIP_T_BOT = 1.0              !   [degC] default = -1.9</span>
<span id="L819">                                ! Temperature at the bottom (interface)</span>
<span id="L820">ISOMIP_S_BOT = 34.7             !   [ppt] default = 34.55</span>
<span id="L821">                                ! Salinity at the bottom (interface)</span>
<span id="L822">DEPRESS_INITIAL_SURFACE = False !   [Boolean] default = False</span>
<span id="L823">                                ! If true,  depress the initial surface to avoid huge tsunamis when a large</span>
<span id="L824">                                ! surface pressure is applied.</span>
<span id="L825">TRIM_IC_FOR_P_SURF = True       !   [Boolean] default = False</span>
<span id="L826">                                ! If true, cuts way the top of the column for initial conditions at the depth</span>
<span id="L827">                                ! where the hydrostatic pressure matches the imposed surface pressure which is</span>
<span id="L828">                                ! read from file.</span>
<span id="L829">SURFACE_PRESSURE_FILE = &quot;Ocean0_3D_Claire.nc&quot; !</span>
<span id="L830">                                ! The initial condition file for the surface pressure exerted by ice.</span>
<span id="L831">SURFACE_PRESSURE_VAR = &quot;thick&quot;  ! default = &quot;&quot;</span>
<span id="L832">                                ! The initial condition variable for the surface pressure exerted by ice.</span>
<span id="L833">SURFACE_PRESSURE_SCALE = 8820.0 !   [file dependent] default = 1.0</span>
<span id="L834">                                ! A scaling factor to convert SURFACE_PRESSURE_VAR from file</span>
<span id="L835">                                ! SURFACE_PRESSURE_FILE into a surface pressure.</span>
<span id="L836">TRIM_IC_Z_TOLERANCE = 1.0E-10   !   [m] default = 1.0E-05</span>
<span id="L837">                                ! The tolerance with which to find the depth matching the specified surface</span>
<span id="L838">                                ! pressure with TRIM_IC_FOR_P_SURF.</span>
<span id="L839">FRAC_DP_AT_POS_NEGATIVE_P_BUGFIX = False !   [Boolean] default = False</span>
<span id="L840">                                ! If true, use bugfix in ice shelf TRIM_IC initialization. Otherwise, pressure</span>
<span id="L841">                                ! input to density EOS is negative.</span>
<span id="L842">TRIMMING_USES_REMAPPING = True  !   [Boolean] default = False</span>
<span id="L843">                                ! When trimming the column, also remap T and S.</span>
<span id="L844">REGRID_ACCELERATE_INIT = False  !   [Boolean] default = False</span>
<span id="L845">                                ! If true, runs REGRID_ACCELERATE_ITERATIONS iterations of the regridding</span>
<span id="L846">                                ! algorithm to push the initial grid to be consistent with the initial</span>
<span id="L847">                                ! condition. Useful only for state-based and iterative coordinates.</span>
<span id="L848">VELOCITY_CONFIG = &quot;zero&quot;        ! default = &quot;zero&quot;</span>
<span id="L849">                                ! A string that determines how the initial velocities are specified for a new</span>
<span id="L850">                                ! run:</span>
<span id="L851">                                !     file - read velocities from the file specified</span>
<span id="L852">                                !       by (VELOCITY_FILE).</span>
<span id="L853">                                !     zero - the fluid is initially at rest.</span>
<span id="L854">                                !     uniform - the flow is uniform (determined by</span>
<span id="L855">                                !       parameters INITIAL_U_CONST and INITIAL_V_CONST).</span>
<span id="L856">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L857">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L858">                                !     USER - call a user modified routine.</span>
<span id="L859">ODA_INCUPD = False              !   [Boolean] default = False</span>
<span id="L860">                                ! If true, oda incremental updates will be applied everywhere in the domain.</span>
<span id="L861">SPONGE = True                   !   [Boolean] default = False</span>
<span id="L862">                                ! If true, sponges may be applied anywhere in the domain. The exact location and</span>
<span id="L863">                                ! properties of those sponges are specified via SPONGE_CONFIG.</span>
<span id="L864">SPONGE_CONFIG = &quot;ISOMIP&quot;        ! default = &quot;file&quot;</span>
<span id="L865">                                ! A string that sets how the sponges are configured:</span>
<span id="L866">                                !     file - read sponge properties from the file</span>
<span id="L867">                                !       specified by (SPONGE_FILE).</span>
<span id="L868">                                !     ISOMIP - apply ale sponge in the ISOMIP case</span>
<span id="L869">                                !     RGC - apply sponge in the rotating_gravity_current case</span>
<span id="L870">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L871">                                !       DOME sill-overflow test case.</span>
<span id="L872">                                !     BFB - Sponge at the southern boundary of the domain</span>
<span id="L873">                                !       for buoyancy-forced basin case.</span>
<span id="L874">                                !     USER - call a user modified routine.</span>
<span id="L875">ISOMIP_TNUDG = 0.1              !   [days] default = 0.0</span>
<span id="L876">                                ! Nudging time scale for sponge layers</span>
<span id="L877">ISOMIP_S_SUR_SPONGE = 33.8      !   [ppt] default = 35.0</span>
<span id="L878">                                ! Surface salinity in sponge layer.</span>
<span id="L879">ISOMIP_S_BOT_SPONGE = 34.7      !   [ppt] default = 35.0</span>
<span id="L880">                                ! Bottom salinity in sponge layer.</span>
<span id="L881">ISOMIP_T_SUR_SPONGE = -1.9      !   [degC] default = 10.0</span>
<span id="L882">                                ! Surface temperature in sponge layer.</span>
<span id="L883">ISOMIP_T_BOT_SPONGE = 1.0       !   [degC] default = 10.0</span>
<span id="L884">                                ! Bottom temperature in sponge layer.</span>
<span id="L885"></span>
<span id="L886">! === module MOM_sponge ===</span>
<span id="L887">SPONGE_UV = False               !   [Boolean] default = False</span>
<span id="L888">                                ! Apply sponges in u and v, in addition to tracers.</span>
<span id="L889">SPONGE_REMAPPING_SCHEME = &quot;PPM_H4&quot; ! default = &quot;PPM_H4&quot;</span>
<span id="L890">                                ! This sets the reconstruction scheme used for vertical remapping for all SPONGE</span>
<span id="L891">                                ! variables.</span>
<span id="L892">SPONGE_BOUNDARY_EXTRAP = False  !   [Boolean] default = False</span>
<span id="L893">                                ! If true, values at the interfaces of SPONGE boundary cells are extrapolated</span>
<span id="L894">                                ! instead of piecewise constant</span>
<span id="L895">SPONGE_REMAPPING_USE_OM4_SUBCELLS = False !   [Boolean] default = False</span>
<span id="L896">                                ! If true, use the OM4 remapping-via-subcells algorithm for ALE sponge. See</span>
<span id="L897">                                ! REMAPPING_USE_OM4_SUBCELLS for more details. We recommend setting this option</span>
<span id="L898">                                ! to false.</span>
<span id="L899">HOR_REGRID_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L900">                                ! The vintage of the order of arithmetic for horizontal regridding.  Dates</span>
<span id="L901">                                ! before 20190101 give the same answers as the code did in late 2018, while</span>
<span id="L902">                                ! later versions add parentheses for rotational symmetry.  Dates after 20230101</span>
<span id="L903">                                ! use reproducing sums for global averages.</span>
<span id="L904">!Total sponge columns at h points = 200 !</span>
<span id="L905">                                ! The total number of columns where sponges are applied at h points.</span>
<span id="L906"></span>
<span id="L907">! === module MOM_diag_mediator ===</span>
<span id="L908">NUM_DIAG_COORDS = 1             ! default = 1</span>
<span id="L909">                                ! The number of diagnostic vertical coordinates to use. For each coordinate, an</span>
<span id="L910">                                ! entry in DIAG_COORDS must be provided.</span>
<span id="L911">DIAG_REMAPPING_USE_OM4_SUBCELLS = False !   [Boolean] default = False</span>
<span id="L912">                                ! If true, use the OM4 remapping-via-subcells algorithm for diagnostics. See</span>
<span id="L913">                                ! REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting this option to</span>
<span id="L914">                                ! false.</span>
<span id="L915">USE_INDEX_DIAGNOSTIC_AXES = False !   [Boolean] default = False</span>
<span id="L916">                                ! If true, use a grid index coordinate convention for diagnostic axes.</span>
<span id="L917">DIAG_COORDS = &quot;z Z ZSTAR&quot;       ! default = &quot;z Z ZSTAR&quot;</span>
<span id="L918">                                ! A list of string tuples associating diag_table modules to a coordinate</span>
<span id="L919">                                ! definition used for diagnostics. Each string is of the form &quot;MODULE_SUFFIX</span>
<span id="L920">                                ! PARAMETER_SUFFIX COORDINATE_NAME&quot;.</span>
<span id="L921">DIAG_MISVAL = 1.0E+20           !   [various] default = 1.0E+20</span>
<span id="L922">                                ! Set the default missing value to use for diagnostics.</span>
<span id="L923">DIAG_AS_CHKSUM = False          !   [Boolean] default = False</span>
<span id="L924">                                ! Instead of writing diagnostics to the diag manager, write a text file</span>
<span id="L925">                                ! containing the checksum (bitcount) of the array.</span>
<span id="L926">AVAILABLE_DIAGS_FILE = &quot;available_diags.000000&quot; ! default = &quot;available_diags.000000&quot;</span>
<span id="L927">                                ! A file into which to write a list of all available ocean diagnostics that can</span>
<span id="L928">                                ! be included in a diag_table.</span>
<span id="L929">DIAG_COORD_DEF_Z = &quot;UNIFORM&quot;    ! default = &quot;UNIFORM&quot;</span>
<span id="L930">                                ! Determines how to specify the coordinate resolution. Valid options are:</span>
<span id="L931">                                !  PARAM       - use the vector-parameter DIAG_COORD_RES_Z</span>
<span id="L932">                                !  UNIFORM[:N] - uniformly distributed</span>
<span id="L933">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L934">                                !                the filename and variable name, separated</span>
<span id="L935">                                !                by a comma or space, e.g. FILE:lev.nc,dz</span>
<span id="L936">                                !                or FILE:lev.nc,interfaces=zw</span>
<span id="L937">                                !  WOA09[:N]   - the WOA09 vertical grid (approximately)</span>
<span id="L938">                                !  WOA09INT[:N] - layers spanned by the WOA09 depths</span>
<span id="L939">                                !  WOA23INT[:N] - layers spanned by the WOA23 depths</span>
<span id="L940">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L941">                                !  HYBRID:string - read from a file. The string specifies</span>
<span id="L942">                                !                the filename and two variable names, separated</span>
<span id="L943">                                !                by a comma or space, for sigma-2 and dz.</span>
<span id="L944">                                !                e.g. HYBRID:vgrid.nc,sigma2,dz</span>
<span id="L945">                                !  HYBRID_3D:string - read from a file. The string specifies</span>
<span id="L946">                                !                the filename and two 3D variable names, separated</span>
<span id="L947">                                !                by a comma or space, for sigma-2 and dz. The</span>
<span id="L948">                                !                latter can be FNC1:string which is used everywhere.</span>
<span id="L949">                                !                e.g. HYBRID_3D:vgrid.nc,sigma2,dz</span>
<span id="L950">                                !  HYBRID_MAP:string - read from a file. The string specifies</span>
<span id="L951">                                !                the filename and three variable names, separated</span>
<span id="L952">                                !                by a comma or space, for map, sigma-2 and dz.</span>
<span id="L953">                                !                Map is a spatial index array with, maxval(map)=N,</span>
<span id="L954">                                !                and the others are 2D arrays containing N profiles.</span>
<span id="L955">                                !                Map typically contains integer values, but it can</span>
<span id="L956">                                !                contain real values, I+w, which imply using</span>
<span id="L957">                                !                the weighted sum of profiles I and I+1.</span>
<span id="L958">                                !                Dz can be FNC1:string which is used everywhere.</span>
<span id="L959">                                !                e.g. HYBRID_MAP:vgrid.nc,map,sigma2,dz</span>
<span id="L960"></span>
<span id="L961">! === module MOM_MEKE ===</span>
<span id="L962">USE_MEKE = False                !   [Boolean] default = False</span>
<span id="L963">                                ! If true, turns on the MEKE scheme which calculates a sub-grid mesoscale eddy</span>
<span id="L964">                                ! kinetic energy budget.</span>
<span id="L965"></span>
<span id="L966">! === module MOM_lateral_mixing_coeffs ===</span>
<span id="L967">USE_VARIABLE_MIXING = False     !   [Boolean] default = False</span>
<span id="L968">                                ! If true, the variable mixing code will be called.  This allows diagnostics to</span>
<span id="L969">                                ! be created even if the scheme is not used.  If KHTR_SLOPE_CFF&gt;0 or</span>
<span id="L970">                                ! KhTh_Slope_Cff&gt;0, this is set to true regardless of what is in the parameter</span>
<span id="L971">                                ! file.</span>
<span id="L972">USE_VISBECK = False             !   [Boolean] default = False</span>
<span id="L973">                                ! If true, use the Visbeck et al. (1997) formulation for</span>
<span id="L974">                                ! thickness diffusivity.</span>
<span id="L975">RESOLN_SCALED_KH = False        !   [Boolean] default = False</span>
<span id="L976">                                ! If true, the Laplacian lateral viscosity is scaled away when the first</span>
<span id="L977">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L978">DEPTH_SCALED_KHTH = False       !   [Boolean] default = False</span>
<span id="L979">                                ! If true, KHTH is scaled away when the depth is shallowerthan a reference</span>
<span id="L980">                                ! depth: KHTH = MIN(1,H/H0)**N * KHTH, where H0 is a reference depth, controlled</span>
<span id="L981">                                ! via DEPTH_SCALED_KHTH_H0, and the exponent (N) is controlled via</span>
<span id="L982">                                ! DEPTH_SCALED_KHTH_EXP.</span>
<span id="L983">RESOLN_SCALED_KHTH = False      !   [Boolean] default = False</span>
<span id="L984">                                ! If true, the interface depth diffusivity is scaled away when the first</span>
<span id="L985">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L986">RESOLN_SCALED_KHTR = False      !   [Boolean] default = False</span>
<span id="L987">                                ! If true, the epipycnal tracer diffusivity is scaled away when the first</span>
<span id="L988">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L989">RESOLN_USE_EBT = False          !   [Boolean] default = False</span>
<span id="L990">                                ! If true, uses the equivalent barotropic wave speed instead of first baroclinic</span>
<span id="L991">                                ! wave for calculating the resolution fn.</span>
<span id="L992">BACKSCAT_EBT_POWER = 0.0        !   [nondim] default = 0.0</span>
<span id="L993">                                ! Power to raise EBT vertical structure to when backscatter has vertical</span>
<span id="L994">                                ! structure.</span>
<span id="L995">BS_USE_SQG_STRUCT = False       !   [Boolean] default = False</span>
<span id="L996">                                ! If true, the SQG vertical structure is used for backscatter on the condition</span>
<span id="L997">                                ! that BS_EBT_power=0</span>
<span id="L998">KHTH_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L999">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L1000">                                ! thickness diffusivity.</span>
<span id="L1001">KHTH_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L1002">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L1003">                                ! of thickness diffusivity.</span>
<span id="L1004">KHTR_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L1005">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L1006">                                ! tracer diffusivity.</span>
<span id="L1007">KHTR_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L1008">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L1009">                                ! of tracer diffusivity.</span>
<span id="L1010">KD_GL90_USE_EBT_STRUCT = False  !   [Boolean] default = False</span>
<span id="L1011">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L1012">                                ! diffusivity in the GL90 scheme.</span>
<span id="L1013">KD_GL90_USE_SQG_STRUCT = False  !   [Boolean] default = False</span>
<span id="L1014">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L1015">                                ! diffusivity in the GL90 scheme.</span>
<span id="L1016">KHTH_SLOPE_CFF = 0.0            !   [nondim] default = 0.0</span>
<span id="L1017">                                ! The nondimensional coefficient in the Visbeck formula for the interface depth</span>
<span id="L1018">                                ! diffusivity</span>
<span id="L1019">KHTR_SLOPE_CFF = 0.0            !   [nondim] default = 0.0</span>
<span id="L1020">                                ! The nondimensional coefficient in the Visbeck formula for the epipycnal tracer</span>
<span id="L1021">                                ! diffusivity</span>
<span id="L1022">USE_STORED_SLOPES = False       !   [Boolean] default = False</span>
<span id="L1023">                                ! If true, the isopycnal slopes are calculated once and stored for re-use. This</span>
<span id="L1024">                                ! uses more memory but avoids calling the equation of state more times than</span>
<span id="L1025">                                ! should be necessary.</span>
<span id="L1026">VERY_SMALL_FREQUENCY = 1.0E-17  !   [s-1] default = 1.0E-17</span>
<span id="L1027">                                ! A miniscule frequency that is used to avoid division by 0.  The default value</span>
<span id="L1028">                                ! is roughly (pi / (the age of the universe)).</span>
<span id="L1029">USE_STANLEY_ISO = False         !   [Boolean] default = False</span>
<span id="L1030">                                ! If true, turn on Stanley SGS T variance parameterization in isopycnal slope</span>
<span id="L1031">                                ! code.</span>
<span id="L1032">KD_SMOOTH = 1.0E-06             !   [m2 s-1] default = 1.0E-06</span>
<span id="L1033">                                ! A diapycnal diffusivity that is used to interpolate more sensible values of T</span>
<span id="L1034">                                ! &amp; S into thin layers.</span>
<span id="L1035">USE_QG_LEITH_GM = False         !   [Boolean] default = False</span>
<span id="L1036">                                ! If true, use the QG Leith viscosity as the GM coefficient.</span>
<span id="L1037"></span>
<span id="L1038">! === module MOM_set_visc ===</span>
<span id="L1039">SET_VISC_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1040">                                ! The vintage of the order of arithmetic and expressions in the set viscosity</span>
<span id="L1041">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1042">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1043">BOTTOMDRAGLAW = True            !   [Boolean] default = True</span>
<span id="L1044">                                ! If true, the bottom stress is calculated with a drag law of the form</span>
<span id="L1045">                                ! c_drag*|u|*u. The velocity magnitude may be an assumed value or it may be</span>
<span id="L1046">                                ! based on the actual velocity in the bottommost HBBL, depending on LINEAR_DRAG.</span>
<span id="L1047">DRAG_AS_BODY_FORCE = False      !   [Boolean] default = False</span>
<span id="L1048">                                ! If true, the bottom stress is imposed as an explicit body force applied over a</span>
<span id="L1049">                                ! fixed distance from the bottom, rather than as an implicit calculation based</span>
<span id="L1050">                                ! on an enhanced near-bottom viscosity. The thickness of the bottom boundary</span>
<span id="L1051">                                ! layer is HBBL.</span>
<span id="L1052">CHANNEL_DRAG = False            !   [Boolean] default = False</span>
<span id="L1053">                                ! If true, the bottom drag is exerted directly on each layer proportional to the</span>
<span id="L1054">                                ! fraction of the bottom it overlies.</span>
<span id="L1055">LINEAR_DRAG = True              !   [Boolean] default = False</span>
<span id="L1056">                                ! If LINEAR_DRAG and BOTTOMDRAGLAW are defined the drag law is</span>
<span id="L1057">                                ! cdrag*DRAG_BG_VEL*u.</span>
<span id="L1058">DYNAMIC_VISCOUS_ML = False      !   [Boolean] default = False</span>
<span id="L1059">                                ! If true, use a bulk Richardson number criterion to determine the mixed layer</span>
<span id="L1060">                                ! thickness for viscosity.</span>
<span id="L1061">OMEGA = 7.2921E-05              !   [s-1] default = 7.2921E-05</span>
<span id="L1062">                                ! The rotation rate of the earth.</span>
<span id="L1063">HBBL = 10.0                     !   [m]</span>
<span id="L1064">                                ! The thickness of a bottom boundary layer with a viscosity increased by</span>
<span id="L1065">                                ! KV_EXTRA_BBL if BOTTOMDRAGLAW is not defined, or the thickness over which</span>
<span id="L1066">                                ! near-bottom velocities are averaged for the drag law if BOTTOMDRAGLAW is</span>
<span id="L1067">                                ! defined but LINEAR_DRAG is not.</span>
<span id="L1068">CDRAG = 0.003                   !   [nondim] default = 0.003</span>
<span id="L1069">                                ! CDRAG is the drag coefficient relating the magnitude of the velocity field to</span>
<span id="L1070">                                ! the bottom stress. CDRAG is only used if BOTTOMDRAGLAW is defined.</span>
<span id="L1071">BBL_USE_TIDAL_BG = False        !   [Boolean] default = False</span>
<span id="L1072">                                ! Flag to use the tidal RMS amplitude in place of constant background velocity</span>
<span id="L1073">                                ! for computing u* in the BBL. This flag is only used when BOTTOMDRAGLAW is true</span>
<span id="L1074">                                ! and LINEAR_DRAG is false.</span>
<span id="L1075">DRAG_BG_VEL = 0.05              !   [m s-1] default = 0.0</span>
<span id="L1076">                                ! DRAG_BG_VEL is either the assumed bottom velocity (with LINEAR_DRAG) or an</span>
<span id="L1077">                                ! unresolved  velocity that is combined with the resolved velocity to estimate</span>
<span id="L1078">                                ! the velocity magnitude.  DRAG_BG_VEL is only used when BOTTOMDRAGLAW is</span>
<span id="L1079">                                ! defined.</span>
<span id="L1080">BBL_USE_EOS = True              !   [Boolean] default = True</span>
<span id="L1081">                                ! If true, use the equation of state in determining the properties of the bottom</span>
<span id="L1082">                                ! boundary layer.  Otherwise use the layer target potential densities.  The</span>
<span id="L1083">                                ! default of this parameter is the value of USE_EOS.</span>
<span id="L1084">BBL_THICK_MIN = 2.0             !   [m] default = 0.0</span>
<span id="L1085">                                ! The minimum bottom boundary layer thickness that can be used with</span>
<span id="L1086">                                ! BOTTOMDRAGLAW. This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum</span>
<span id="L1087">                                ! near-bottom viscosity.</span>
<span id="L1088">HTBL_SHELF_MIN = 2.0            !   [m] default = 2.0</span>
<span id="L1089">                                ! The minimum top boundary layer thickness that can be used with BOTTOMDRAGLAW.</span>
<span id="L1090">                                ! This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum near-top</span>
<span id="L1091">                                ! viscosity.</span>
<span id="L1092">HTBL_SHELF = 10.0               !   [m] default = 10.0</span>
<span id="L1093">                                ! The thickness over which near-surface velocities are averaged for the drag law</span>
<span id="L1094">                                ! under an ice shelf.  By default this is the same as HBBL</span>
<span id="L1095">KV = 0.001                      !   [m2 s-1]</span>
<span id="L1096">                                ! The background kinematic viscosity in the interior. The molecular value, ~1e-6</span>
<span id="L1097">                                ! m2 s-1, may be used.</span>
<span id="L1098">KV_BBL_MIN = 0.001              !   [m2 s-1] default = 0.001</span>
<span id="L1099">                                ! The minimum viscosities in the bottom boundary layer.</span>
<span id="L1100">KV_TBL_MIN = 0.01               !   [m2 s-1] default = 0.001</span>
<span id="L1101">                                ! The minimum viscosities in the top boundary layer.</span>
<span id="L1102">CORRECT_BBL_BOUNDS = False      !   [Boolean] default = False</span>
<span id="L1103">                                ! If true, uses the correct bounds on the BBL thickness and viscosity so that</span>
<span id="L1104">                                ! the bottom layer feels the intended drag.</span>
<span id="L1105"></span>
<span id="L1106">! === module MOM_thickness_diffuse ===</span>
<span id="L1107">KHTH = 0.0                      !   [m2 s-1] default = 0.0</span>
<span id="L1108">                                ! The background horizontal thickness diffusivity.</span>
<span id="L1109">READ_KHTH = False               !   [Boolean] default = False</span>
<span id="L1110">                                ! If true, read a file (given by KHTH_FILE) containing the spatially varying</span>
<span id="L1111">                                ! horizontal isopycnal height diffusivity.</span>
<span id="L1112">KHTH_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L1113">                                ! The minimum horizontal thickness diffusivity.</span>
<span id="L1114">KHTH_MAX = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L1115">                                ! The maximum horizontal thickness diffusivity.</span>
<span id="L1116">KHTH_MAX_CFL = 0.8              !   [nondimensional] default = 0.8</span>
<span id="L1117">                                ! The maximum value of the local diffusive CFL ratio that is permitted for the</span>
<span id="L1118">                                ! thickness diffusivity. 1.0 is the marginally unstable value in a pure layered</span>
<span id="L1119">                                ! model, but much smaller numbers (e.g. 0.1) seem to work better for ALE-based</span>
<span id="L1120">                                ! models.</span>
<span id="L1121">KH_ETA_CONST = 0.0              !   [m2 s-1] default = 0.0</span>
<span id="L1122">                                ! The background horizontal diffusivity of the interface heights (without</span>
<span id="L1123">                                ! considering the layer density structure).  If diffusive CFL limits are</span>
<span id="L1124">                                ! encountered, the diffusivities of the isopycnals and the interfaces heights</span>
<span id="L1125">                                ! are scaled back proportionately.</span>
<span id="L1126">KH_ETA_VEL_SCALE = 0.0          !   [m s-1] default = 0.0</span>
<span id="L1127">                                ! A velocity scale that is multiplied by the grid spacing to give a contribution</span>
<span id="L1128">                                ! to the horizontal diffusivity of the interface heights (without considering</span>
<span id="L1129">                                ! the layer density structure).</span>
<span id="L1130">DETANGLE_INTERFACES = False     !   [Boolean] default = False</span>
<span id="L1131">                                ! If defined add 3-d structured enhanced interface height diffusivities to</span>
<span id="L1132">                                ! horizontally smooth jagged layers.</span>
<span id="L1133">KHTH_SLOPE_MAX = 0.01           !   [nondim] default = 0.01</span>
<span id="L1134">                                ! A slope beyond which the calculated isopycnal slope is not reliable and is</span>
<span id="L1135">                                ! scaled away.</span>
<span id="L1136">KHTH_USE_FGNV_STREAMFUNCTION = False !   [Boolean] default = False</span>
<span id="L1137">                                ! If true, use the streamfunction formulation of Ferrari et al., 2010, which</span>
<span id="L1138">                                ! effectively emphasizes graver vertical modes by smoothing in the vertical.</span>
<span id="L1139">USE_STANLEY_GM = False          !   [Boolean] default = False</span>
<span id="L1140">                                ! If true, turn on Stanley SGS T variance parameterization in GM code.</span>
<span id="L1141">MEKE_GM_SRC_ALT = False         !   [Boolean] default = False</span>
<span id="L1142">                                ! If true, use the GM energy conversion form S^2*N^2*kappa rather than the</span>
<span id="L1143">                                ! streamfunction for the GM source term.</span>
<span id="L1144">MEKE_GEOMETRIC = False          !   [Boolean] default = False</span>
<span id="L1145">                                ! If true, uses the GM coefficient formulation from the GEOMETRIC framework</span>
<span id="L1146">                                ! (Marshall et al., 2012).</span>
<span id="L1147">USE_GME = False                 !   [Boolean] default = False</span>
<span id="L1148">                                ! If true, use the GM+E backscatter scheme in association with the Gent and</span>
<span id="L1149">                                ! McWilliams parameterization.</span>
<span id="L1150">USE_GM_WORK_BUG = False         !   [Boolean] default = False</span>
<span id="L1151">                                ! If true, compute the top-layer work tendency on the u-grid with the incorrect</span>
<span id="L1152">                                ! sign, for legacy reproducibility.</span>
<span id="L1153">STOCH_EOS = False               !   [Boolean] default = False</span>
<span id="L1154">                                ! If true, stochastic perturbations are applied to the EOS in the PGF.</span>
<span id="L1155">STANLEY_COEFF = -1.0            !   [nondim] default = -1.0</span>
<span id="L1156">                                ! Coefficient correlating the temperature gradient and SGS T variance.</span>
<span id="L1157"></span>
<span id="L1158">! === module MOM_dynamics_split_RK2 ===</span>
<span id="L1159">TIDES = False                   !   [Boolean] default = False</span>
<span id="L1160">                                ! If true, apply tidal momentum forcing.</span>
<span id="L1161">CALCULATE_SAL = False           !   [Boolean] default = False</span>
<span id="L1162">                                ! If true, calculate self-attraction and loading.</span>
<span id="L1163">USE_HA = False                  !   [Boolean] default = False</span>
<span id="L1164">                                ! If true, perform inline harmonic analysis.</span>
<span id="L1165">BE = 0.7                        !   [nondim] default = 0.6</span>
<span id="L1166">                                ! If SPLIT is true, BE determines the relative weighting of a  2nd-order</span>
<span id="L1167">                                ! Runga-Kutta baroclinic time stepping scheme (0.5) and a backward Euler scheme</span>
<span id="L1168">                                ! (1) that is used for the Coriolis and inertial terms.  BE may be from 0.5 to</span>
<span id="L1169">                                ! 1, but instability may occur near 0.5. BE is also applicable if SPLIT is false</span>
<span id="L1170">                                ! and USE_RK2 is true.</span>
<span id="L1171">BEGW = 0.0                      !   [nondim] default = 0.0</span>
<span id="L1172">                                ! If SPLIT is true, BEGW is a number from 0 to 1 that controls the extent to</span>
<span id="L1173">                                ! which the treatment of gravity waves is forward-backward (0) or simulated</span>
<span id="L1174">                                ! backward Euler (1).  0 is almost always used. If SPLIT is false and USE_RK2 is</span>
<span id="L1175">                                ! true, BEGW can be between 0 and 0.5 to damp gravity waves.</span>
<span id="L1176">SET_DTBT_USE_BT_CONT = False    !   [Boolean] default = False</span>
<span id="L1177">                                ! If true, use BT_CONT to calculate DTBT if possible.</span>
<span id="L1178">SPLIT_BOTTOM_STRESS = False     !   [Boolean] default = False</span>
<span id="L1179">                                ! If true, provide the bottom stress calculated by the vertical viscosity to the</span>
<span id="L1180">                                ! barotropic solver.</span>
<span id="L1181">BT_USE_LAYER_FLUXES = True      !   [Boolean] default = True</span>
<span id="L1182">                                ! If true, use the summed layered fluxes plus an adjustment due to the change in</span>
<span id="L1183">                                ! the barotropic velocity in the barotropic continuity equation.</span>
<span id="L1184">BT_ADJ_CORR_MASS_SRC = True     !   [Boolean] default = True</span>
<span id="L1185">                                ! If true, recalculates the barotropic mass source after predictor step. This</span>
<span id="L1186">                                ! should make little difference in the deep ocean but appears to help for</span>
<span id="L1187">                                ! vanished layers. If false, uses the same mass source as from the predictor</span>
<span id="L1188">                                ! step.</span>
<span id="L1189">STORE_CORIOLIS_ACCEL = True     !   [Boolean] default = True</span>
<span id="L1190">                                ! If true, calculate the Coriolis accelerations at the end of each timestep for</span>
<span id="L1191">                                ! use in the predictor step of the next split RK2 timestep.</span>
<span id="L1192">FPMIX = False                   !   [Boolean] default = False</span>
<span id="L1193">                                ! If true, add non-local momentum flux increments and diffuse down the Eulerian</span>
<span id="L1194">                                ! gradient.</span>
<span id="L1195">VISC_REM_BUG = False            !   [Boolean] default = False</span>
<span id="L1196">                                ! If true, visc_rem_[uv] in split mode is incorrectly calculated or accounted</span>
<span id="L1197">                                ! for in two places. This parameter controls the defaults of two individual</span>
<span id="L1198">                                ! flags, VISC_REM_TIMESTEP_BUG in MOM_dynamics_split_RK2(b) and</span>
<span id="L1199">                                ! VISC_REM_BT_WEIGHT_BUG in MOM_barotropic.</span>
<span id="L1200">VISC_REM_TIMESTEP_BUG = False   !   [Boolean] default = False</span>
<span id="L1201">                                ! If true, recover a bug that uses dt_pred rather than dt in vertvisc_remnant()</span>
<span id="L1202">                                ! at the end of predictor stage for the following continuity() and btstep()</span>
<span id="L1203">                                ! calls in the corrector step. Default of this flag is set by VISC_REM_BUG</span>
<span id="L1204"></span>
<span id="L1205">! === module MOM_continuity_PPM ===</span>
<span id="L1206">MONOTONIC_CONTINUITY = False    !   [Boolean] default = False</span>
<span id="L1207">                                ! If true, CONTINUITY_PPM uses the Colella and Woodward monotonic limiter.  The</span>
<span id="L1208">                                ! default (false) is to use a simple positive definite limiter.</span>
<span id="L1209">SIMPLE_2ND_PPM_CONTINUITY = False !   [Boolean] default = False</span>
<span id="L1210">                                ! If true, CONTINUITY_PPM uses a simple 2nd order (arithmetic mean)</span>
<span id="L1211">                                ! interpolation of the edge values. This may give better PV conservation</span>
<span id="L1212">                                ! properties. While it formally reduces the accuracy of the continuity solver</span>
<span id="L1213">                                ! itself in the strongly advective limit, it does not reduce the overall order</span>
<span id="L1214">                                ! of accuracy of the dynamic core.</span>
<span id="L1215">UPWIND_1ST_CONTINUITY = False   !   [Boolean] default = False</span>
<span id="L1216">                                ! If true, CONTINUITY_PPM becomes a 1st-order upwind continuity solver.  This</span>
<span id="L1217">                                ! scheme is highly diffusive but may be useful for debugging or in single-column</span>
<span id="L1218">                                ! mode where its minimal stencil is useful.</span>
<span id="L1219">ETA_TOLERANCE = 1.0E-12         !   [m] default = 1.8E-14</span>
<span id="L1220">                                ! The tolerance for the differences between the barotropic and baroclinic</span>
<span id="L1221">                                ! estimates of the sea surface height due to the fluxes through each face.  The</span>
<span id="L1222">                                ! total tolerance for SSH is 4 times this value.  The default is</span>
<span id="L1223">                                ! 0.5*NK*ANGSTROM, and this should not be set less than about</span>
<span id="L1224">                                ! 10^-15*MAXIMUM_DEPTH.</span>
<span id="L1225">VELOCITY_TOLERANCE = 3.0E+08    !   [m s-1] default = 3.0E+08</span>
<span id="L1226">                                ! The tolerance for barotropic velocity discrepancies between the barotropic</span>
<span id="L1227">                                ! solution and  the sum of the layer thicknesses.</span>
<span id="L1228">CONT_PPM_AGGRESS_ADJUST = False !   [Boolean] default = False</span>
<span id="L1229">                                ! If true, allow the adjusted velocities to have a relative CFL change up to</span>
<span id="L1230">                                ! 0.5.</span>
<span id="L1231">CONT_PPM_VOLUME_BASED_CFL = False !   [Boolean] default = False</span>
<span id="L1232">                                ! If true, use the ratio of the open face lengths to the tracer cell areas when</span>
<span id="L1233">                                ! estimating CFL numbers.  The default is set by CONT_PPM_AGGRESS_ADJUST.</span>
<span id="L1234">CONTINUITY_CFL_LIMIT = 0.5      !   [nondim] default = 0.5</span>
<span id="L1235">                                ! The maximum CFL of the adjusted velocities.</span>
<span id="L1236">CONT_PPM_BETTER_ITER = True     !   [Boolean] default = True</span>
<span id="L1237">                                ! If true, stop corrective iterations using a velocity based criterion and only</span>
<span id="L1238">                                ! stop if the iteration is better than all predecessors.</span>
<span id="L1239">CONT_PPM_USE_VISC_REM_MAX = True !   [Boolean] default = True</span>
<span id="L1240">                                ! If true, use more appropriate limiting bounds for corrections in strongly</span>
<span id="L1241">                                ! viscous columns.</span>
<span id="L1242">CONT_PPM_MARGINAL_FACE_AREAS = True !   [Boolean] default = True</span>
<span id="L1243">                                ! If true, use the marginal face areas from the continuity solver for use as the</span>
<span id="L1244">                                ! weights in the barotropic solver. Otherwise use the transport averaged areas.</span>
<span id="L1245"></span>
<span id="L1246">! === module MOM_CoriolisAdv ===</span>
<span id="L1247">NOSLIP = False                  !   [Boolean] default = False</span>
<span id="L1248">                                ! If true, no slip boundary conditions are used; otherwise free slip boundary</span>
<span id="L1249">                                ! conditions are assumed. The implementation of the free slip BCs on a C-grid is</span>
<span id="L1250">                                ! much cleaner than the no slip BCs. The use of free slip BCs is strongly</span>
<span id="L1251">                                ! encouraged, and no slip BCs are not used with the biharmonic viscosity.</span>
<span id="L1252">CORIOLIS_EN_DIS = True          !   [Boolean] default = False</span>
<span id="L1253">                                ! If true, two estimates of the thickness fluxes are used to estimate the</span>
<span id="L1254">                                ! Coriolis term, and the one that dissipates energy relative to the other one is</span>
<span id="L1255">                                ! used.</span>
<span id="L1256">CORIOLIS_SCHEME = &quot;SADOURNY75_ENERGY&quot; ! default = &quot;SADOURNY75_ENERGY&quot;</span>
<span id="L1257">                                ! CORIOLIS_SCHEME selects the discretization for the Coriolis terms. Valid</span>
<span id="L1258">                                ! values are:</span>
<span id="L1259">                                !    SADOURNY75_ENERGY - Sadourny, 1975; energy cons.</span>
<span id="L1260">                                !    ARAKAWA_HSU90     - Arakawa &amp; Hsu, 1990</span>
<span id="L1261">                                !    SADOURNY75_ENSTRO - Sadourny, 1975; enstrophy cons.</span>
<span id="L1262">                                !    ARAKAWA_LAMB81    - Arakawa &amp; Lamb, 1981; En. + Enst.</span>
<span id="L1263">                                !    ARAKAWA_LAMB_BLEND - A blend of Arakawa &amp; Lamb with</span>
<span id="L1264">                                !                         Arakawa &amp; Hsu and Sadourny energy</span>
<span id="L1265">                                !    WENOVI5TH_PV_ENSTRO   - 5th-order WENO PV enstrophy</span>
<span id="L1266">                                !    WENOVI3RD_PV_ENSTRO   - 3rd-order WENO PV enstrophy</span>
<span id="L1267">                                !    WENOVI7TH_PV_ENSTRO  - 7th-order WENO PV enstrophy</span>
<span id="L1268">BOUND_CORIOLIS = True           !   [Boolean] default = False</span>
<span id="L1269">                                ! If true, the Coriolis terms at u-points are bounded by the four estimates of</span>
<span id="L1270">                                ! (f+rv)v from the four neighboring v-points, and similarly at v-points.  This</span>
<span id="L1271">                                ! option is always effectively false with CORIOLIS_EN_DIS defined and</span>
<span id="L1272">                                ! CORIOLIS_SCHEME set to SADOURNY75_ENERGY.</span>
<span id="L1273">KE_SCHEME = &quot;KE_ARAKAWA&quot;        ! default = &quot;KE_ARAKAWA&quot;</span>
<span id="L1274">                                ! KE_SCHEME selects the discretization for acceleration due to the kinetic</span>
<span id="L1275">                                ! energy gradient. Valid values are:</span>
<span id="L1276">                                !    KE_ARAKAWA, KE_SIMPLE_GUDONOV, KE_GUDONOV, KE_UP3</span>
<span id="L1277">PV_ADV_SCHEME = &quot;PV_ADV_CENTERED&quot; ! default = &quot;PV_ADV_CENTERED&quot;</span>
<span id="L1278">                                ! PV_ADV_SCHEME selects the discretization for PV advection. Valid values are:</span>
<span id="L1279">                                !    PV_ADV_CENTERED - centered (aka Sadourny, 75)</span>
<span id="L1280">                                !    PV_ADV_UPWIND1  - upwind, first order</span>
<span id="L1281"></span>
<span id="L1282">! === module MOM_PressureForce ===</span>
<span id="L1283">ANALYTIC_FV_PGF = True          !   [Boolean] default = True</span>
<span id="L1284">                                ! If true the pressure gradient forces are calculated with a finite volume form</span>
<span id="L1285">                                ! that analytically integrates the equations of state in pressure to avoid any</span>
<span id="L1286">                                ! possibility of numerical thermobaric instability, as described in Adcroft et</span>
<span id="L1287">                                ! al., O. Mod. (2008).</span>
<span id="L1288"></span>
<span id="L1289">! === module MOM_PressureForce_FV ===</span>
<span id="L1290">RHO_PGF_REF = 1027.0            !   [kg m-3] default = 1027.0</span>
<span id="L1291">                                ! The reference density that is subtracted off when calculating pressure</span>
<span id="L1292">                                ! gradient forces.  Its inverse is subtracted off of specific volumes when in</span>
<span id="L1293">                                ! non-Boussinesq mode.  The default is RHO_0.</span>
<span id="L1294">RHO_PGF_REF_BUG = True          !   [Boolean] default = True</span>
<span id="L1295">                                ! If true, recover a bug that RHO_0 (the mean seawater density in Boussinesq</span>
<span id="L1296">                                ! mode) and RHO_PGF_REF (the subtracted reference density in finite volume</span>
<span id="L1297">                                ! pressure gradient forces) are incorrectly interchanged in several instances in</span>
<span id="L1298">                                ! Boussinesq mode.</span>
<span id="L1299">SSH_IN_EOS_PRESSURE_FOR_PGF = False !   [Boolean] default = False</span>
<span id="L1300">                                ! If true, include contributions from the sea surface height in the height-based</span>
<span id="L1301">                                ! pressure used in the equation of state calculations for the Boussinesq</span>
<span id="L1302">                                ! pressure gradient forces, including adjustments for atmospheric or sea-ice</span>
<span id="L1303">                                ! pressure.</span>
<span id="L1304">MASS_WEIGHT_IN_PRESSURE_GRADIENT = True !   [Boolean] default = False</span>
<span id="L1305">                                ! If true, use mass weighting when interpolating T/S for integrals near the</span>
<span id="L1306">                                ! bathymetry in FV pressure gradient calculations.</span>
<span id="L1307">MASS_WEIGHT_IN_PRESSURE_GRADIENT_TOP = True !   [Boolean] default = True</span>
<span id="L1308">                                ! If true and MASS_WEIGHT_IN_PRESSURE_GRADIENT is true, use mass weighting when</span>
<span id="L1309">                                ! interpolating T/S for integrals near the top of the water column in FV</span>
<span id="L1310">                                ! pressure gradient calculations.</span>
<span id="L1311">MASS_WEIGHT_IN_PGF_VANISHED_ONLY = True !   [Boolean] default = False</span>
<span id="L1312">                                ! If true, use mass weighting when interpolating T/S for integrals only if one</span>
<span id="L1313">                                ! side is vanished according to RESET_INTXPA_H_NONVANISHED.</span>
<span id="L1314">CORRECTION_INTXPA = False       !   [Boolean] default = False</span>
<span id="L1315">                                ! If true, use a correction for surface pressure curvature in intx_pa.</span>
<span id="L1316">RESET_INTXPA_INTEGRAL = True    !   [Boolean] default = False</span>
<span id="L1317">                                ! If true, reset INTXPA to match pressures at first nonvanished cell. Includes</span>
<span id="L1318">                                ! pressure correction.</span>
<span id="L1319">RESET_INTXPA_INTEGRAL_FLATTEST = True !   [Boolean] default = False</span>
<span id="L1320">                                ! If true, use flattest interface as reference interface where there is no</span>
<span id="L1321">                                ! better choice for RESET_INTXPA_INTEGRAL. Otherwise, use surface interface.</span>
<span id="L1322">RESET_INTXPA_H_NONVANISHED = 1.0E-06 !   [m] default = 1.0E-06</span>
<span id="L1323">                                ! A minimal layer thickness that indicates that a layer is thick enough to</span>
<span id="L1324">                                ! usefully reestimate the pressure integral across the interface below.</span>
<span id="L1325">USE_INACCURATE_PGF_RHO_ANOM = False !   [Boolean] default = False</span>
<span id="L1326">                                ! If true, use a form of the PGF that uses the reference density in an</span>
<span id="L1327">                                ! inaccurate way. This is not recommended.</span>
<span id="L1328">RECONSTRUCT_FOR_PRESSURE = True !   [Boolean] default = True</span>
<span id="L1329">                                ! If True, use vertical reconstruction of T &amp; S within the integrals of the FV</span>
<span id="L1330">                                ! pressure gradient calculation. If False, use the constant-by-layer algorithm.</span>
<span id="L1331">                                ! The default is set by USE_REGRIDDING.</span>
<span id="L1332">PRESSURE_RECONSTRUCTION_SCHEME = 1 ! default = 1</span>
<span id="L1333">                                ! Order of vertical reconstruction of T/S to use in the integrals within the FV</span>
<span id="L1334">                                ! pressure gradient calculation.</span>
<span id="L1335">                                !  0: PCM or no reconstruction.</span>
<span id="L1336">                                !  1: PLM reconstruction.</span>
<span id="L1337">                                !  2: PPM reconstruction.</span>
<span id="L1338">BOUNDARY_EXTRAPOLATION_PRESSURE = True !   [Boolean] default = True</span>
<span id="L1339">                                ! If true, the reconstruction of T &amp; S for pressure in boundary cells is</span>
<span id="L1340">                                ! extrapolated, rather than using PCM in these cells. If true, the same order</span>
<span id="L1341">                                ! polynomial is used as is used for the interior cells.</span>
<span id="L1342">USE_STANLEY_PGF = False         !   [Boolean] default = False</span>
<span id="L1343">                                ! If true, turn on Stanley SGS T variance parameterization in PGF code.</span>
<span id="L1344"></span>
<span id="L1345">! === module MOM_Zanna_Bolton ===</span>
<span id="L1346">USE_ZB2020 = False              !   [Boolean] default = False</span>
<span id="L1347">                                ! If true, turns on Zanna-Bolton-2020 (ZB) subgrid momentum parameterization of</span>
<span id="L1348">                                ! mesoscale eddies.</span>
<span id="L1349"></span>
<span id="L1350">! === module MOM_hor_visc ===</span>
<span id="L1351">USE_CIRCULATION_IN_HORVISC = False !   [Boolean] default = False</span>
<span id="L1352">                                ! Use circulation theorem to compute vorticity in horvisc module (for ZB20 or</span>
<span id="L1353">                                ! Leith)</span>
<span id="L1354">USE_CONT_THICKNESS = False      !   [Boolean] default = False</span>
<span id="L1355">                                ! If true, use thickness at velocity points from continuity solver. This option</span>
<span id="L1356">                                ! currently only works with split mode.</span>
<span id="L1357">LAPLACIAN = True                !   [Boolean] default = False</span>
<span id="L1358">                                ! If true, use a Laplacian horizontal viscosity.</span>
<span id="L1359">KH = 6.0                        !   [m2 s-1] default = 0.0</span>
<span id="L1360">                                ! The background Laplacian horizontal viscosity.</span>
<span id="L1361">KH_BG_MIN = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1362">                                ! The minimum value allowed for Laplacian horizontal viscosity, KH.</span>
<span id="L1363">KH_VEL_SCALE = 0.0              !   [m s-1] default = 0.0</span>
<span id="L1364">                                ! The velocity scale which is multiplied by the grid spacing to calculate the</span>
<span id="L1365">                                ! Laplacian viscosity. The final viscosity is the largest of this scaled</span>
<span id="L1366">                                ! viscosity, the Smagorinsky and Leith viscosities, and KH.</span>
<span id="L1367">KH_SIN_LAT = 0.0                !   [m2 s-1] default = 0.0</span>
<span id="L1368">                                ! The amplitude of a latitudinally-dependent background viscosity of the form</span>
<span id="L1369">                                ! KH_SIN_LAT*(SIN(LAT)**KH_PWR_OF_SINE).</span>
<span id="L1370">SMAGORINSKY_KH = False          !   [Boolean] default = False</span>
<span id="L1371">                                ! If true, use a Smagorinsky nonlinear eddy viscosity.</span>
<span id="L1372">LEITH_KH = False                !   [Boolean] default = False</span>
<span id="L1373">                                ! If true, use a Leith nonlinear eddy viscosity.</span>
<span id="L1374">BOUND_KH = True                 !   [Boolean] default = True</span>
<span id="L1375">                                ! If true, the Laplacian coefficient is locally limited to be stable.</span>
<span id="L1376">EY24_EBT_BS = False             !   [Boolean] default = False</span>
<span id="L1377">                                ! If true, use the the backscatter scheme (EBT mode with kill switch)developed</span>
<span id="L1378">                                ! by Yankovsky et al. (2024).</span>
<span id="L1379">ANISOTROPIC_VISCOSITY = False   !   [Boolean] default = False</span>
<span id="L1380">                                ! If true, allow anistropic viscosity in the Laplacian horizontal viscosity.</span>
<span id="L1381">ADD_LES_VISCOSITY = False       !   [Boolean] default = False</span>
<span id="L1382">                                ! If true, adds the viscosity from Smagorinsky and Leith to the background</span>
<span id="L1383">                                ! viscosity instead of taking the maximum.</span>
<span id="L1384">BIHARMONIC = True               !   [Boolean] default = True</span>
<span id="L1385">                                ! If true, use a biharmonic horizontal viscosity. BIHARMONIC may be used with</span>
<span id="L1386">                                ! LAPLACIAN.</span>
<span id="L1387">AH = 0.0                        !   [m4 s-1] default = 0.0</span>
<span id="L1388">                                ! The background biharmonic horizontal viscosity.</span>
<span id="L1389">AH_VEL_SCALE = 0.001            !   [m s-1] default = 0.0</span>
<span id="L1390">                                ! The velocity scale which is multiplied by the cube of the grid spacing to</span>
<span id="L1391">                                ! calculate the biharmonic viscosity. The final viscosity is the largest of this</span>
<span id="L1392">                                ! scaled viscosity, the Smagorinsky and Leith viscosities, and AH.</span>
<span id="L1393">AH_TIME_SCALE = 0.0             !   [s] default = 0.0</span>
<span id="L1394">                                ! A time scale whose inverse is multiplied by the fourth power of the grid</span>
<span id="L1395">                                ! spacing to calculate biharmonic viscosity. The final viscosity is the largest</span>
<span id="L1396">                                ! of all viscosity formulations in use. 0.0 means that it&#x27;s not used.</span>
<span id="L1397">SMAGORINSKY_AH = True           !   [Boolean] default = False</span>
<span id="L1398">                                ! If true, use a biharmonic Smagorinsky nonlinear eddy viscosity.</span>
<span id="L1399">LEITH_AH = False                !   [Boolean] default = False</span>
<span id="L1400">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity.</span>
<span id="L1401">USE_LEITHY = False              !   [Boolean] default = False</span>
<span id="L1402">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity together with a</span>
<span id="L1403">                                ! harmonic backscatter.</span>
<span id="L1404">BOUND_AH = True                 !   [Boolean] default = True</span>
<span id="L1405">                                ! If true, the biharmonic coefficient is locally limited to be stable.</span>
<span id="L1406">RE_AH = 0.0                     !   [nondim] default = 0.0</span>
<span id="L1407">                                ! If nonzero, the biharmonic coefficient is scaled so that the biharmonic</span>
<span id="L1408">                                ! Reynolds number is equal to this.</span>
<span id="L1409">BACKSCATTER_UNDERBOUND = True   !   [Boolean] default = False</span>
<span id="L1410">                                ! If true, the bounds on the biharmonic viscosity are allowed to increase where</span>
<span id="L1411">                                ! the Laplacian viscosity is negative (due to backscatter parameterizations)</span>
<span id="L1412">                                ! beyond the largest timestep-dependent stable values of biharmonic viscosity</span>
<span id="L1413">                                ! when no Laplacian viscosity is applied.  The default is true for historical</span>
<span id="L1414">                                ! reasons, but this option probably should not be used because it can contribute</span>
<span id="L1415">                                ! to numerical instabilities.</span>
<span id="L1416">SMAG_BI_CONST = 0.06            !   [nondim] default = 0.0</span>
<span id="L1417">                                ! The nondimensional biharmonic Smagorinsky constant, typically 0.015 - 0.06.</span>
<span id="L1418">BOUND_CORIOLIS_BIHARM = True    !   [Boolean] default = True</span>
<span id="L1419">                                ! If true use a viscosity that increases with the square of the velocity shears,</span>
<span id="L1420">                                ! so that the resulting viscous drag is of comparable magnitude to the Coriolis</span>
<span id="L1421">                                ! terms when the velocity differences between adjacent grid points is</span>
<span id="L1422">                                ! 0.5*BOUND_CORIOLIS_VEL.  The default is the value of BOUND_CORIOLIS (or</span>
<span id="L1423">                                ! false).</span>
<span id="L1424">BOUND_CORIOLIS_VEL = 10.0       !   [m s-1] default = 10.0</span>
<span id="L1425">                                ! The velocity scale at which BOUND_CORIOLIS_BIHARM causes the biharmonic drag</span>
<span id="L1426">                                ! to have comparable magnitude to the Coriolis acceleration.  The default is set</span>
<span id="L1427">                                ! by MAXVEL.</span>
<span id="L1428">USE_LAND_MASK_FOR_HVISC = True  !   [Boolean] default = True</span>
<span id="L1429">                                ! If true, use the land mask for the computation of thicknesses at velocity</span>
<span id="L1430">                                ! locations. This eliminates the dependence on arbitrary values over land or</span>
<span id="L1431">                                ! outside of the domain.</span>
<span id="L1432">HORVISC_BOUND_COEF = 0.8        !   [nondim] default = 0.8</span>
<span id="L1433">                                ! The nondimensional coefficient of the ratio of the viscosity bounds to the</span>
<span id="L1434">                                ! theoretical maximum for stability without considering other terms.</span>
<span id="L1435">USE_KH_BG_2D = False            !   [Boolean] default = False</span>
<span id="L1436">                                ! If true, read a file containing 2-d background harmonic viscosities. The final</span>
<span id="L1437">                                ! viscosity is the maximum of the other terms and this background value.</span>
<span id="L1438">FRICTWORK_BUG = False           !   [Boolean] default = False</span>
<span id="L1439">                                ! If true, retain an answer-changing bug in calculating the FrictWork, which</span>
<span id="L1440">                                ! cancels the h in thickness flux and the h at velocity point. This isnot</span>
<span id="L1441">                                ! recommended.</span>
<span id="L1442"></span>
<span id="L1443">! === module MOM_vert_friction ===</span>
<span id="L1444">VERT_FRICTION_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1445">                                ! The vintage of the order of arithmetic and expressions in the viscous</span>
<span id="L1446">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1447">                                ! while higher values use expressions that do not use an arbitrary hard-coded</span>
<span id="L1448">                                ! maximum viscous coupling coefficient between layers.  Values below 20230601</span>
<span id="L1449">                                ! recover a form of the viscosity within the mixed layer that breaks up the</span>
<span id="L1450">                                ! magnitude of the wind stress in some non-Boussinesq cases.</span>
<span id="L1451">DIRECT_STRESS = False           !   [Boolean] default = False</span>
<span id="L1452">                                ! If true, the wind stress is distributed over the topmost HMIX_STRESS of fluid</span>
<span id="L1453">                                ! (like in HYCOM), and an added mixed layer viscosity or a physically based</span>
<span id="L1454">                                ! boundary layer turbulence parameterization is not needed for stability.</span>
<span id="L1455">FIXED_DEPTH_LOTW_ML = False     !   [Boolean] default = False</span>
<span id="L1456">                                ! If true, use a Law-of-the-wall prescription for the mixed layer viscosity</span>
<span id="L1457">                                ! within a boundary layer that is the lesser of HMIX_FIXED and the total depth</span>
<span id="L1458">                                ! of the ocean in a column.</span>
<span id="L1459">LOTW_VISCOUS_ML_FLOOR = False   !   [Boolean] default = False</span>
<span id="L1460">                                ! If true, use a Law-of-the-wall prescription to set a lower bound on the</span>
<span id="L1461">                                ! viscous coupling between layers within the surface boundary layer, based the</span>
<span id="L1462">                                ! distance of interfaces from the surface.  This only acts when there are large</span>
<span id="L1463">                                ! changes in the thicknesses of successive layers or when the viscosity is set</span>
<span id="L1464">                                ! externally and the wind stress has subsequently increased.</span>
<span id="L1465">VON_KARMAN_CONST = 0.41         !   [nondim] default = 0.41</span>
<span id="L1466">                                ! The value the von Karman constant as used for mixed layer viscosity.</span>
<span id="L1467">HARMONIC_VISC = False           !   [Boolean] default = False</span>
<span id="L1468">                                ! If true, use the harmonic mean thicknesses for calculating the vertical</span>
<span id="L1469">                                ! viscosity.</span>
<span id="L1470">HARMONIC_BL_SCALE = 1.0         !   [nondim] default = 0.0</span>
<span id="L1471">                                ! A scale to determine when water is in the boundary layers based solely on</span>
<span id="L1472">                                ! harmonic mean thicknesses for the purpose of determining the extent to which</span>
<span id="L1473">                                ! the thicknesses used in the viscosities are upwinded.</span>
<span id="L1474">HMIX_FIXED = 20.0               !   [m]</span>
<span id="L1475">                                ! The prescribed depth over which the near-surface viscosity and diffusivity are</span>
<span id="L1476">                                ! elevated when the bulk mixed layer is not used.</span>
<span id="L1477">USE_GL90_IN_SSW = False         !   [Boolean] default = False</span>
<span id="L1478">                                ! If true, use simpler method to calculate 1/N^2 in GL90 vertical viscosity</span>
<span id="L1479">                                ! coefficient. This method is valid in stacked shallow water mode.</span>
<span id="L1480">KV_ML_INVZ2 = 0.0               !   [m2 s-1] default = 0.0</span>
<span id="L1481">                                ! An extra kinematic viscosity in a mixed layer of thickness HMIX_FIXED, with</span>
<span id="L1482">                                ! the actual viscosity scaling as 1/(z*HMIX_FIXED)^2, where z is the distance</span>
<span id="L1483">                                ! from the surface, to allow for finite wind stresses to be transmitted through</span>
<span id="L1484">                                ! infinitesimally thin surface layers.  This is an older option for numerical</span>
<span id="L1485">                                ! convenience without a strong physical basis, and its use is now discouraged.</span>
<span id="L1486">CFL_TRUNCATE = 0.5              !   [nondim] default = 0.5</span>
<span id="L1487">                                ! The value of the CFL number that will cause velocity components to be</span>
<span id="L1488">                                ! truncated; instability can occur past 0.5.</span>
<span id="L1489">CFL_REPORT = 0.5                !   [nondim] default = 0.5</span>
<span id="L1490">                                ! The value of the CFL number that causes accelerations to be reported; the</span>
<span id="L1491">                                ! default is CFL_TRUNCATE.</span>
<span id="L1492">CFL_TRUNCATE_RAMP_TIME = 0.0    !   [s] default = 0.0</span>
<span id="L1493">                                ! The time over which the CFL truncation value is ramped up at the beginning of</span>
<span id="L1494">                                ! the run.</span>
<span id="L1495">CFL_TRUNCATE_START = 0.0        !   [nondim] default = 0.0</span>
<span id="L1496">                                ! The start value of the truncation CFL number used when ramping up CFL_TRUNC.</span>
<span id="L1497">STOKES_MIXING_COMBINED = False  !   [Boolean] default = False</span>
<span id="L1498">                                ! Flag to use Stokes drift Mixing via the Lagrangian  current (Eulerian plus</span>
<span id="L1499">                                ! Stokes drift).  Still needs work and testing, so not recommended for use.</span>
<span id="L1500">VEL_UNDERFLOW = 0.0             !   [m s-1] default = 0.0</span>
<span id="L1501">                                ! A negligibly small velocity magnitude below which velocity components are set</span>
<span id="L1502">                                ! to 0.  A reasonable value might be 1e-30 m/s, which is less than an Angstrom</span>
<span id="L1503">                                ! divided by the age of the universe.</span>
<span id="L1504"></span>
<span id="L1505">! === module MOM_barotropic ===</span>
<span id="L1506">USE_BT_CONT_TYPE = True         !   [Boolean] default = True</span>
<span id="L1507">                                ! If true, use a structure with elements that describe effective face areas from</span>
<span id="L1508">                                ! the summed continuity solver as a function the barotropic flow in coupling</span>
<span id="L1509">                                ! between the barotropic and baroclinic flow.  This is only used if SPLIT is</span>
<span id="L1510">                                ! true.</span>
<span id="L1511">INTEGRAL_BT_CONTINUITY = False  !   [Boolean] default = False</span>
<span id="L1512">                                ! If true, use the time-integrated velocity over the barotropic steps to</span>
<span id="L1513">                                ! determine the integrated transports used to update the continuity equation.</span>
<span id="L1514">                                ! Otherwise the transports are the sum of the transports based on a series of</span>
<span id="L1515">                                ! instantaneous velocities and the BT_CONT_TYPE for transports.  This is only</span>
<span id="L1516">                                ! valid if USE_BT_CONT_TYPE = True.</span>
<span id="L1517">BOUND_BT_CORRECTION = True      !   [Boolean] default = False</span>
<span id="L1518">                                ! If true, the corrective pseudo mass-fluxes into the barotropic solver are</span>
<span id="L1519">                                ! limited to values that require less than maxCFL_BT_cont to be accommodated.</span>
<span id="L1520">BT_CONT_CORR_BOUNDS = True      !   [Boolean] default = True</span>
<span id="L1521">                                ! If true, and BOUND_BT_CORRECTION is true, use the BT_cont_type variables to</span>
<span id="L1522">                                ! set limits determined by MAXCFL_BT_CONT on the CFL number of the velocities</span>
<span id="L1523">                                ! that are likely to be driven by the corrective mass fluxes.</span>
<span id="L1524">ADJUST_BT_CONT = False          !   [Boolean] default = False</span>
<span id="L1525">                                ! If true, adjust the curve fit to the BT_cont type that is used by the</span>
<span id="L1526">                                ! barotropic solver to match the transport about which the flow is being</span>
<span id="L1527">                                ! linearized.</span>
<span id="L1528">GRADUAL_BT_ICS = False          !   [Boolean] default = False</span>
<span id="L1529">                                ! If true, adjust the initial conditions for the barotropic solver to the values</span>
<span id="L1530">                                ! from the layered solution over a whole timestep instead of instantly. This is</span>
<span id="L1531">                                ! a decent approximation to the inclusion of sum(u dh_dt) while also correcting</span>
<span id="L1532">                                ! for truncation errors.</span>
<span id="L1533">BT_USE_VISC_REM_U_UH0 = False   !   [Boolean] default = False</span>
<span id="L1534">                                ! If true, use the viscous remnants when estimating the barotropic velocities</span>
<span id="L1535">                                ! that were used to calculate uh0 and vh0.  False is probably the better choice.</span>
<span id="L1536">BT_PROJECT_VELOCITY = False     !   [Boolean] default = False</span>
<span id="L1537">                                ! If true, step the barotropic velocity first and project out the velocity</span>
<span id="L1538">                                ! tendency by 1+BEBT when calculating the transport.  The default (false) is to</span>
<span id="L1539">                                ! use a predictor continuity step to find the pressure field, and then to do a</span>
<span id="L1540">                                ! corrector continuity step using a weighted average of the old and new</span>
<span id="L1541">                                ! velocities, with weights of (1-BEBT) and BEBT.</span>
<span id="L1542">BT_NONLIN_STRESS = False        !   [Boolean] default = False</span>
<span id="L1543">                                ! If true, use the full depth of the ocean at the start of the barotropic step</span>
<span id="L1544">                                ! when calculating the surface stress contribution to the barotropic</span>
<span id="L1545">                                ! acclerations.  Otherwise use the depth based on bathyT.</span>
<span id="L1546">DYNAMIC_SURFACE_PRESSURE = True !   [Boolean] default = False</span>
<span id="L1547">                                ! If true, add a dynamic pressure due to a viscous ice shelf, for instance.</span>
<span id="L1548">ICE_LENGTH_DYN_PSURF = 1.0E+04  !   [m] default = 1.0E+04</span>
<span id="L1549">                                ! The length scale at which the Rayleigh damping rate due to the ice strength</span>
<span id="L1550">                                ! should be the same as if a Laplacian were applied, if DYNAMIC_SURFACE_PRESSURE</span>
<span id="L1551">                                ! is true.</span>
<span id="L1552">DEPTH_MIN_DYN_PSURF = 1.0E-06   !   [m] default = 1.0E-06</span>
<span id="L1553">                                ! The minimum depth to use in limiting the size of the dynamic surface pressure</span>
<span id="L1554">                                ! for stability, if DYNAMIC_SURFACE_PRESSURE is true..</span>
<span id="L1555">CONST_DYN_PSURF = 0.9           !   [nondim] default = 0.9</span>
<span id="L1556">                                ! The constant that scales the dynamic surface pressure, if</span>
<span id="L1557">                                ! DYNAMIC_SURFACE_PRESSURE is true.  Stable values are &lt; ~1.0.</span>
<span id="L1558">BT_CORIOLIS_SCALE = 1.0         !   [nondim] default = 1.0</span>
<span id="L1559">                                ! A factor by which the barotropic Coriolis anomaly terms are scaled.</span>
<span id="L1560">BAROTROPIC_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1561">                                ! The vintage of the expressions in the barotropic solver. Values below 20190101</span>
<span id="L1562">                                ! recover the answers from the end of 2018, while higher values use more</span>
<span id="L1563">                                ! efficient or general expressions.</span>
<span id="L1564">VISC_REM_BT_WEIGHT_BUG = False  !   [Boolean] default = False</span>
<span id="L1565">                                ! If true, recover a bug in barotropic solver that uses an unnormalized weight</span>
<span id="L1566">                                ! function for vertical averages of baroclinic velocity and forcing. Default of</span>
<span id="L1567">                                ! this flag is set by VISC_REM_BUG.</span>
<span id="L1568">TIDAL_SAL_FLATHER = False       !   [Boolean] default = False</span>
<span id="L1569">                                ! If true, then apply adjustments to the external gravity wave speed used with</span>
<span id="L1570">                                ! the Flather OBC routine consistent with the barotropic solver. This applies to</span>
<span id="L1571">                                ! cases with  tidal forcing using the scalar self-attraction approximation. The</span>
<span id="L1572">                                ! default is currently False in order to retain previous answers but should be</span>
<span id="L1573">                                ! set to True for new experiments</span>
<span id="L1574">SADOURNY = True                 !   [Boolean] default = True</span>
<span id="L1575">                                ! If true, the Coriolis terms are discretized with the Sadourny (1975) energy</span>
<span id="L1576">                                ! conserving scheme, otherwise the Arakawa &amp; Hsu scheme is used.  If the</span>
<span id="L1577">                                ! internal deformation radius is not resolved, the Sadourny scheme should</span>
<span id="L1578">                                ! probably be used.</span>
<span id="L1579">BT_THICK_SCHEME = &quot;FROM_BT_CONT&quot; ! default = &quot;FROM_BT_CONT&quot;</span>
<span id="L1580">                                ! A string describing the scheme that is used to set the open face areas used</span>
<span id="L1581">                                ! for barotropic transport and the relative weights of the accelerations. Valid</span>
<span id="L1582">                                ! values are:</span>
<span id="L1583">                                !    ARITHMETIC - arithmetic mean layer thicknesses</span>
<span id="L1584">                                !    HARMONIC - harmonic mean layer thicknesses</span>
<span id="L1585">                                !    HYBRID (the default) - use arithmetic means for</span>
<span id="L1586">                                !       layers above the shallowest bottom, the harmonic</span>
<span id="L1587">                                !       mean for layers below, and a weighted average for</span>
<span id="L1588">                                !       layers that straddle that depth</span>
<span id="L1589">                                !    FROM_BT_CONT - use the average thicknesses kept</span>
<span id="L1590">                                !       in the h_u and h_v fields of the BT_cont_type</span>
<span id="L1591">BT_STRONG_DRAG = True           !   [Boolean] default = False</span>
<span id="L1592">                                ! If true, use a stronger estimate of the retarding effects of strong bottom</span>
<span id="L1593">                                ! drag, by making it implicit with the barotropic time-step instead of implicit</span>
<span id="L1594">                                ! with the baroclinic time-step and dividing by the number of barotropic steps.</span>
<span id="L1595">RESCALE_STRONG_DRAG = True      !   [Boolean] default = False</span>
<span id="L1596">                                ! If true, reduce the barotropic contribution to the layer accelerations to</span>
<span id="L1597">                                ! account for the difference between the forces that can be counteracted by the</span>
<span id="L1598">                                ! stronger drag with BT_STRONG_DRAG and the average of the layer viscous</span>
<span id="L1599">                                ! remnants after a baroclinic timestep.</span>
<span id="L1600">BT_LINEAR_WAVE_DRAG = False     !   [Boolean] default = False</span>
<span id="L1601">                                ! If true, apply a linear drag to the barotropic velocities, using rates set by</span>
<span id="L1602">                                ! lin_drag_u &amp; _v divided by the depth of the ocean.  This was introduced to</span>
<span id="L1603">                                ! facilitate tide modeling.</span>
<span id="L1604">BT_LINEAR_FREQ_DRAG = False     !   [Boolean] default = False</span>
<span id="L1605">                                ! If true, apply frequency-dependent drag to the tidal velocities. The streaming</span>
<span id="L1606">                                ! band-pass filter must be turned on.</span>
<span id="L1607">CLIP_BT_VELOCITY = False        !   [Boolean] default = False</span>
<span id="L1608">                                ! If true, limit any velocity components that exceed CFL_TRUNCATE.  This should</span>
<span id="L1609">                                ! only be used as a desperate debugging measure.</span>
<span id="L1610">MAXCFL_BT_CONT = 0.25           !   [nondim] default = 0.25</span>
<span id="L1611">                                ! The maximum permitted CFL number associated with the barotropic accelerations</span>
<span id="L1612">                                ! from the summed velocities times the time-derivatives of thicknesses.</span>
<span id="L1613">DT_BT_FILTER = -0.25            !   [sec or nondim] default = -0.25</span>
<span id="L1614">                                ! A time-scale over which the barotropic mode solutions are filtered, in seconds</span>
<span id="L1615">                                ! if positive, or as a fraction of DT if negative. When used this can never be</span>
<span id="L1616">                                ! taken to be longer than 2*dt.  Set this to 0 to apply no filtering.</span>
<span id="L1617">G_BT_EXTRA = 0.0                !   [nondim] default = 0.0</span>
<span id="L1618">                                ! A nondimensional factor by which gtot is enhanced.</span>
<span id="L1619">SSH_EXTRA = 10.0                !   [m] default = 10.0</span>
<span id="L1620">                                ! An estimate of how much higher SSH might get, for use in calculating the safe</span>
<span id="L1621">                                ! external wave speed. The default is the minimum of 10 m or 5% of</span>
<span id="L1622">                                ! MAXIMUM_DEPTH.</span>
<span id="L1623">LINEARIZED_BT_CORIOLIS = True   !   [Boolean] default = True</span>
<span id="L1624">                                ! If true use the bottom depth instead of the total water column thickness in</span>
<span id="L1625">                                ! the barotropic Coriolis term calculations.</span>
<span id="L1626">BEBT = 0.2                      !   [nondim] default = 0.1</span>
<span id="L1627">                                ! BEBT determines whether the barotropic time stepping uses the forward-backward</span>
<span id="L1628">                                ! time-stepping scheme or a backward Euler scheme. BEBT is valid in the range</span>
<span id="L1629">                                ! from 0 (for a forward-backward treatment of nonrotating gravity waves) to 1</span>
<span id="L1630">                                ! (for a backward Euler treatment). In practice, BEBT must be greater than about</span>
<span id="L1631">                                ! 0.05.</span>
<span id="L1632">DTBT = -0.9                     !   [s or nondim] default = -0.98</span>
<span id="L1633">                                ! The barotropic time step, in s. DTBT is only used with the split explicit time</span>
<span id="L1634">                                ! stepping. To set the time step automatically based the maximum stable value</span>
<span id="L1635">                                ! use 0, or a negative value gives the fraction of the stable value. Setting</span>
<span id="L1636">                                ! DTBT to 0 is the same as setting it to -0.98. The value of DTBT that will</span>
<span id="L1637">                                ! actually be used is an integer fraction of DT, rounding down.</span>
<span id="L1638">BT_USE_OLD_CORIOLIS_BRACKET_BUG = False !   [Boolean] default = False</span>
<span id="L1639">                                ! If True, use an order of operations that is not bitwise rotationally symmetric</span>
<span id="L1640">                                ! in the meridional Coriolis term of the barotropic solver.</span>
<span id="L1641">MASK_COASTAL_PRESSURE_FORCE = False !   [Boolean] default = False</span>
<span id="L1642">                                ! If true, use the land masks to zero out the diagnosed barotropic pressure</span>
<span id="L1643">                                ! gradient accelerations at coastal or land points.  This changes diagnostics</span>
<span id="L1644">                                ! and improves the reproducibility of certain debugging checksums, but it does</span>
<span id="L1645">                                ! not alter the solutions themselves.</span>
<span id="L1646"></span>
<span id="L1647">! === module MOM_mixed_layer_restrat ===</span>
<span id="L1648">MIXEDLAYER_RESTRAT = False      !   [Boolean] default = False</span>
<span id="L1649">                                ! If true, a density-gradient dependent re-stratifying flow is imposed in the</span>
<span id="L1650">                                ! mixed layer. Can be used in ALE mode without restriction but in layer mode can</span>
<span id="L1651">                                ! only be used if BULKMIXEDLAYER is true.</span>
<span id="L1652"></span>
<span id="L1653">! === module MOM_diagnostics ===</span>
<span id="L1654">DIAG_EBT_MONO_N2_COLUMN_FRACTION = 0.0 !   [nondim] default = 0.0</span>
<span id="L1655">                                ! The lower fraction of water column over which N2 is limited as monotonic for</span>
<span id="L1656">                                ! the purposes of calculating the equivalent barotropic wave speed.</span>
<span id="L1657">DIAG_EBT_MONO_N2_DEPTH = -1.0   !   [m] default = -1.0</span>
<span id="L1658">                                ! The depth below which N2 is limited as monotonic for the purposes of</span>
<span id="L1659">                                ! calculating the equivalent barotropic wave speed.</span>
<span id="L1660">INTERNAL_WAVE_SPEED_TOL = 0.001 !   [nondim] default = 0.001</span>
<span id="L1661">                                ! The fractional tolerance for finding the wave speeds.</span>
<span id="L1662">INTERNAL_WAVE_SPEED_MIN = 0.0   !   [m s-1] default = 0.0</span>
<span id="L1663">                                ! A floor in the first mode speed below which 0 used instead.</span>
<span id="L1664">INTERNAL_WAVE_SPEED_BETTER_EST = True !   [Boolean] default = True</span>
<span id="L1665">                                ! If true, use a more robust estimate of the first mode wave speed as the</span>
<span id="L1666">                                ! starting point for iterations.</span>
<span id="L1667">INTWAVE_REMAPPING_USE_OM4_SUBCELLS = False !   [Boolean] default = False</span>
<span id="L1668">                                ! If true, use the OM4 remapping-via-subcells algorithm for calculating EBT</span>
<span id="L1669">                                ! structure. See REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting</span>
<span id="L1670">                                ! this option to false.</span>
<span id="L1671"></span>
<span id="L1672">! === module MOM_diabatic_driver ===</span>
<span id="L1673">! The following parameters are used for diabatic processes.</span>
<span id="L1674">USE_LEGACY_DIABATIC_DRIVER = True !   [Boolean] default = True</span>
<span id="L1675">                                ! If true, use a legacy version of the diabatic subroutine. This is temporary</span>
<span id="L1676">                                ! and is needed to avoid change in answers.</span>
<span id="L1677">ENERGETICS_SFC_PBL = True       !   [Boolean] default = False</span>
<span id="L1678">                                ! If true, use an implied energetics planetary boundary layer scheme to</span>
<span id="L1679">                                ! determine the diffusivity and viscosity in the surface boundary layer.</span>
<span id="L1680">EPBL_IS_ADDITIVE = True         !   [Boolean] default = True</span>
<span id="L1681">                                ! If true, the diffusivity from ePBL is added to all other diffusivities.</span>
<span id="L1682">                                ! Otherwise, the larger of kappa-shear and ePBL diffusivities are used.</span>
<span id="L1683">PRANDTL_EPBL = 1.0              !   [nondim] default = 1.0</span>
<span id="L1684">                                ! The Prandtl number used by ePBL to convert vertical diffusivities into</span>
<span id="L1685">                                ! viscosities.</span>
<span id="L1686">INTERNAL_TIDES = False          !   [Boolean] default = False</span>
<span id="L1687">                                ! If true, use the code that advances a separate set of equations for the</span>
<span id="L1688">                                ! internal tide energy density.</span>
<span id="L1689">MASSLESS_MATCH_TARGETS = True   !   [Boolean] default = True</span>
<span id="L1690">                                ! If true, the temperature and salinity of massless layers are kept consistent</span>
<span id="L1691">                                ! with their target densities. Otherwise the properties of massless layers</span>
<span id="L1692">                                ! evolve diffusively to match massive neighboring layers.</span>
<span id="L1693">AGGREGATE_FW_FORCING = True     !   [Boolean] default = True</span>
<span id="L1694">                                ! If true, the net incoming and outgoing fresh water fluxes are combined and</span>
<span id="L1695">                                ! applied as either incoming or outgoing depending on the sign of the net. If</span>
<span id="L1696">                                ! false, the net incoming fresh water flux is added to the model and thereafter</span>
<span id="L1697">                                ! the net outgoing is removed from the topmost non-vanished layers of the</span>
<span id="L1698">                                ! updated state.</span>
<span id="L1699">MIX_BOUNDARY_TRACERS = True     !   [Boolean] default = True</span>
<span id="L1700">                                ! If true, mix the passive tracers in massless layers at the bottom into the</span>
<span id="L1701">                                ! interior as though a diffusivity of KD_MIN_TR were operating.</span>
<span id="L1702">MIX_BOUNDARY_TRACER_ALE = False !   [Boolean] default = False</span>
<span id="L1703">                                ! If true and in ALE mode, mix the passive tracers in massless layers at the</span>
<span id="L1704">                                ! bottom into the interior as though a diffusivity of KD_MIN_TR were operating.</span>
<span id="L1705">KD_MIN_TR = 5.0E-06             !   [m2 s-1] default = 5.0E-06</span>
<span id="L1706">                                ! A minimal diffusivity that should always be applied to tracers, especially in</span>
<span id="L1707">                                ! massless layers near the bottom. The default is 0.1*KD.</span>
<span id="L1708">KD_BBL_TR = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1709">                                ! A bottom boundary layer tracer diffusivity that will allow for explicitly</span>
<span id="L1710">                                ! specified bottom fluxes. The entrainment at the bottom is at least</span>
<span id="L1711">                                ! sqrt(Kd_BBL_tr*dt) over the same distance.</span>
<span id="L1712">TRACER_TRIDIAG = False          !   [Boolean] default = False</span>
<span id="L1713">                                ! If true, use the passive tracer tridiagonal solver for T and S</span>
<span id="L1714">MINIMUM_FORCING_DEPTH = 1.0     !   [m] default = 0.001</span>
<span id="L1715">                                ! The smallest depth over which forcing can be applied. This only takes effect</span>
<span id="L1716">                                ! when near-surface layers become thin relative to this scale, in which case the</span>
<span id="L1717">                                ! forcing tendencies scaled down by distributing the forcing over this depth</span>
<span id="L1718">                                ! scale.</span>
<span id="L1719">EVAP_CFL_LIMIT = 0.8            !   [nondim] default = 0.8</span>
<span id="L1720">                                ! The largest fraction of a layer than can be lost to forcing (e.g. evaporation,</span>
<span id="L1721">                                ! sea-ice formation) in one time-step. The unused mass loss is passed down</span>
<span id="L1722">                                ! through the column.</span>
<span id="L1723">MLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1724">                                ! The energy values used to compute MLDs.  If not set (or all set to 0.), the</span>
<span id="L1725">                                ! default will overwrite to 25., 2500., 250000.</span>
<span id="L1726">BMLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1727">                                ! The energy values used to compute Bottom MLDs.  If not set (or all set to 0.),</span>
<span id="L1728">                                ! the default will overwrite to 25., 2500., 250000.</span>
<span id="L1729">DIAG_MLD_DENSITY_DIFF = 0.1     !   [kg/m3] default = 0.1</span>
<span id="L1730">                                ! The density difference used to determine a diagnostic mixed layer depth,</span>
<span id="L1731">                                ! MLD_user, following the definition of Levitus 1982. The MLD is the depth at</span>
<span id="L1732">                                ! which the density is larger than the surface density by the specified amount.</span>
<span id="L1733">DIAG_DEPTH_SUBML_N2 = 50.0      !   [m] default = 50.0</span>
<span id="L1734">                                ! The distance over which to calculate a diagnostic of the stratification at the</span>
<span id="L1735">                                ! base of the mixed layer.</span>
<span id="L1736"></span>
<span id="L1737">! === module MOM_CVMix_KPP ===</span>
<span id="L1738">! This is the MOM wrapper to CVMix:KPP</span>
<span id="L1739">! See http://cvmix.github.io/</span>
<span id="L1740">USE_KPP = False                 !   [Boolean] default = False</span>
<span id="L1741">                                ! If true, turns on the [CVMix] KPP scheme of Large et al., 1994, to calculate</span>
<span id="L1742">                                ! diffusivities and non-local transport in the OBL.</span>
<span id="L1743"></span>
<span id="L1744">! === module MOM_CVMix_conv ===</span>
<span id="L1745">! Parameterization of enhanced mixing due to convection via CVMix</span>
<span id="L1746">USE_CVMix_CONVECTION = False    !   [Boolean] default = False</span>
<span id="L1747">                                ! If true, turns on the enhanced mixing due to convection via CVMix. This scheme</span>
<span id="L1748">                                ! increases diapycnal diffs./viscs. at statically unstable interfaces. Relevant</span>
<span id="L1749">                                ! parameters are contained in the CVMix_CONVECTION% parameter block.</span>
<span id="L1750"></span>
<span id="L1751">! === module MOM_set_diffusivity ===</span>
<span id="L1752">FLUX_RI_MAX = 0.2               !   [nondim] default = 0.2</span>
<span id="L1753">                                ! The flux Richardson number where the stratification is large enough that N2 &gt;</span>
<span id="L1754">                                ! omega2.  The full expression for the Flux Richardson number is usually</span>
<span id="L1755">                                ! FLUX_RI_MAX*N2/(N2+OMEGA2).</span>
<span id="L1756">SET_DIFF_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1757">                                ! The vintage of the order of arithmetic and expressions in the set diffusivity</span>
<span id="L1758">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1759">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1760">                                ! Values above 20250301 also use less confusing expressions to set the</span>
<span id="L1761">                                ! bottom-drag generated diffusivity when USE_LOTW_BBL_DIFFUSIVITY is false.</span>
<span id="L1762"></span>
<span id="L1763">! === module MOM_tidal_mixing ===</span>
<span id="L1764">! Vertical Tidal Mixing Parameterization</span>
<span id="L1765">USE_CVMix_TIDAL = False         !   [Boolean] default = False</span>
<span id="L1766">                                ! If true, turns on tidal mixing via CVMix</span>
<span id="L1767">INT_TIDE_DISSIPATION = False    !   [Boolean] default = False</span>
<span id="L1768">                                ! If true, use an internal tidal dissipation scheme to drive diapycnal mixing,</span>
<span id="L1769">                                ! along the lines of St. Laurent et al. (2002) and Simmons et al. (2004).</span>
<span id="L1770">ML_RADIATION = False            !   [Boolean] default = False</span>
<span id="L1771">                                ! If true, allow a fraction of TKE available from wind work to penetrate below</span>
<span id="L1772">                                ! the base of the mixed layer with a vertical decay scale determined by the</span>
<span id="L1773">                                ! minimum of: (1) The depth of the mixed layer, (2) an Ekman length scale.</span>
<span id="L1774">BBL_EFFIC = 0.0                 !   [nondim] default = 0.2</span>
<span id="L1775">                                ! The efficiency with which the energy extracted by bottom drag drives BBL</span>
<span id="L1776">                                ! diffusion.  This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1777">BBL_MIXING_MAX_DECAY = 200.0    !   [m] default = 200.0</span>
<span id="L1778">                                ! The maximum decay scale for the BBL diffusion, or 0 to allow the mixing to</span>
<span id="L1779">                                ! penetrate as far as stratification and rotation permit.  The default for now</span>
<span id="L1780">                                ! is 200 m. This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1781">BBL_MIXING_AS_MAX = True        !   [Boolean] default = True</span>
<span id="L1782">                                ! If true, take the maximum of the diffusivity from the BBL mixing and the other</span>
<span id="L1783">                                ! diffusivities. Otherwise, diffusivity from the BBL_mixing is simply added.</span>
<span id="L1784">USE_LOTW_BBL_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1785">                                ! If true, uses a simple, imprecise but non-coordinate dependent, model of BBL</span>
<span id="L1786">                                ! mixing diffusivity based on Law of the Wall. Otherwise, uses the original BBL</span>
<span id="L1787">                                ! scheme.</span>
<span id="L1788">DZ_BBL_AVG_MIN = 0.0            !   [m] default = 0.0</span>
<span id="L1789">                                ! A minimal distance over which to average to determine the average bottom</span>
<span id="L1790">                                ! boundary layer density.</span>
<span id="L1791">SIMPLE_TKE_TO_KD = False        !   [Boolean] default = False</span>
<span id="L1792">                                ! If true, uses a simple estimate of Kd/TKE that will work for arbitrary</span>
<span id="L1793">                                ! vertical coordinates. If false, calculates Kd/TKE and bounds based on exact</span>
<span id="L1794">                                ! energetics for an isopycnal layer-formulation.</span>
<span id="L1795"></span>
<span id="L1796">! === module MOM_bkgnd_mixing ===</span>
<span id="L1797">! Adding static vertical background mixing coefficients</span>
<span id="L1798">KD = 5.0E-05                    !   [m2 s-1] default = 0.0</span>
<span id="L1799">                                ! The background diapycnal diffusivity of density in the interior. Zero or the</span>
<span id="L1800">                                ! molecular value, ~1e-7 m2 s-1, may be used.</span>
<span id="L1801">KD_MIN = 5.000000000000001E-07  !   [m2 s-1] default = 5.000000000000001E-07</span>
<span id="L1802">                                ! The minimum diapycnal diffusivity.</span>
<span id="L1803">BRYAN_LEWIS_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1804">                                ! If true, use a Bryan &amp; Lewis (JGR 1979) like tanh profile of background</span>
<span id="L1805">                                ! diapycnal diffusivity with depth. This is done via CVMix.</span>
<span id="L1806">HORIZ_VARYING_BACKGROUND = False !   [Boolean] default = False</span>
<span id="L1807">                                ! If true, apply vertically uniform, latitude-dependent background diffusivity,</span>
<span id="L1808">                                ! as described in Danabasoglu et al., 2012</span>
<span id="L1809">PRANDTL_BKGND = 1.0             !   [nondim] default = 1.0</span>
<span id="L1810">                                ! Turbulent Prandtl number used to convert vertical background diffusivities</span>
<span id="L1811">                                ! into viscosities.</span>
<span id="L1812">HENYEY_IGW_BACKGROUND = False   !   [Boolean] default = False</span>
<span id="L1813">                                ! If true, use a latitude-dependent scaling for the near surface background</span>
<span id="L1814">                                ! diffusivity, as described in Harrison &amp; Hallberg, JPO 2008.</span>
<span id="L1815">KD_TANH_LAT_FN = False          !   [Boolean] default = False</span>
<span id="L1816">                                ! If true, use a tanh dependence of Kd_sfc on latitude, like CM2.1/CM2M.  There</span>
<span id="L1817">                                ! is no physical justification for this form, and it can not be used with</span>
<span id="L1818">                                ! HENYEY_IGW_BACKGROUND.</span>
<span id="L1819">KD_MAX = -1.0                   !   [m2 s-1] default = -1.0</span>
<span id="L1820">                                ! The maximum permitted increment for the diapycnal diffusivity from TKE-based</span>
<span id="L1821">                                ! parameterizations, or a negative value for no limit.</span>
<span id="L1822">KD_ADD = 0.0                    !   [m2 s-1] default = 0.0</span>
<span id="L1823">                                ! A uniform diapycnal diffusivity that is added everywhere without any filtering</span>
<span id="L1824">                                ! or scaling.</span>
<span id="L1825">USER_CHANGE_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1826">                                ! If true, call user-defined code to change the diffusivity.</span>
<span id="L1827">DISSIPATION_MIN = 0.0           !   [W m-3] default = 0.0</span>
<span id="L1828">                                ! The minimum dissipation by which to determine a lower bound of Kd (a floor).</span>
<span id="L1829">DISSIPATION_N0 = 0.0            !   [W m-3] default = 0.0</span>
<span id="L1830">                                ! The intercept when N=0 of the N-dependent expression used to set a minimum</span>
<span id="L1831">                                ! dissipation by which to determine a lower bound of Kd (a floor): A in eps_min</span>
<span id="L1832">                                ! = A + B*N.</span>
<span id="L1833">DISSIPATION_N1 = 0.0            !   [J m-3] default = 0.0</span>
<span id="L1834">                                ! The coefficient multiplying N, following Gargett, used to set a minimum</span>
<span id="L1835">                                ! dissipation by which to determine a lower bound of Kd (a floor): B in eps_min</span>
<span id="L1836">                                ! = A + B*N</span>
<span id="L1837">DISSIPATION_KD_MIN = 0.0        !   [m2 s-1] default = 0.0</span>
<span id="L1838">                                ! The minimum vertical diffusivity applied as a floor.</span>
<span id="L1839">DOUBLE_DIFFUSION = False        !   [Boolean] default = False</span>
<span id="L1840">                                ! If true, increase diffusivites for temperature or salinity based on the</span>
<span id="L1841">                                ! double-diffusive parameterization described in Large et al. (1994).</span>
<span id="L1842"></span>
<span id="L1843">! === module MOM_kappa_shear ===</span>
<span id="L1844">! Parameterization of shear-driven turbulence following Jackson, Hallberg and Legg, JPO 2008</span>
<span id="L1845">USE_JACKSON_PARAM = True        !   [Boolean] default = False</span>
<span id="L1846">                                ! If true, use the Jackson-Hallberg-Legg (JPO 2008) shear mixing</span>
<span id="L1847">                                ! parameterization.</span>
<span id="L1848">VERTEX_SHEAR = False            !   [Boolean] default = False</span>
<span id="L1849">                                ! If true, do the calculations of the shear-driven mixing at the cell vertices</span>
<span id="L1850">                                ! (i.e., the vorticity points).</span>
<span id="L1851">VERTEX_SHEAR_THICKNESS_MEAN = False !   [Boolean] default = False</span>
<span id="L1852">                                ! If true, apply thickness weighting to horizontal averagings of diffusivity to</span>
<span id="L1853">                                ! tracer points in the kappa shear solver.</span>
<span id="L1854">RINO_CRIT = 0.25                !   [nondim] default = 0.25</span>
<span id="L1855">                                ! The critical Richardson number for shear mixing.</span>
<span id="L1856">SHEARMIX_RATE = 0.089           !   [nondim] default = 0.089</span>
<span id="L1857">                                ! A nondimensional rate scale for shear-driven entrainment. Jackson et al find</span>
<span id="L1858">                                ! values in the range of 0.085-0.089.</span>
<span id="L1859">MAX_RINO_IT = 50                !   [nondim] default = 50</span>
<span id="L1860">                                ! The maximum number of iterations that may be used to estimate the Richardson</span>
<span id="L1861">                                ! number driven mixing.</span>
<span id="L1862">KD_KAPPA_SHEAR_0 = 5.0E-05      !   [m2 s-1] default = 5.0E-05</span>
<span id="L1863">                                ! The background diffusivity that is used to smooth the density and shear</span>
<span id="L1864">                                ! profiles before solving for the diffusivities.  The default is the greater of</span>
<span id="L1865">                                ! KD and 1e-7 m2 s-1.</span>
<span id="L1866">KD_SEED_KAPPA_SHEAR = 1.0       !   [m2 s-1] default = 1.0</span>
<span id="L1867">                                ! A moderately large seed value of diapycnal diffusivity that is used as a</span>
<span id="L1868">                                ! starting turbulent diffusivity in the iterations to find an energetically</span>
<span id="L1869">                                ! constrained solution for the shear-driven diffusivity.</span>
<span id="L1870">KD_TRUNC_KAPPA_SHEAR = 5.000000000000001E-07 !   [m2 s-1] default = 5.000000000000001E-07</span>
<span id="L1871">                                ! The value of shear-driven diffusivity that is considered negligible and is</span>
<span id="L1872">                                ! rounded down to 0. The default is 1% of KD_KAPPA_SHEAR_0.</span>
<span id="L1873">FRI_CURVATURE = -0.97           !   [nondim] default = -0.97</span>
<span id="L1874">                                ! The nondimensional curvature of the function of the Richardson number in the</span>
<span id="L1875">                                ! kappa source term in the Jackson et al. scheme.</span>
<span id="L1876">TKE_N_DECAY_CONST = 0.24        !   [nondim] default = 0.24</span>
<span id="L1877">                                ! The coefficient for the decay of TKE due to stratification (i.e. proportional</span>
<span id="L1878">                                ! to N*tke). The values found by Jackson et al. are 0.24-0.28.</span>
<span id="L1879">TKE_SHEAR_DECAY_CONST = 0.14    !   [nondim] default = 0.14</span>
<span id="L1880">                                ! The coefficient for the decay of TKE due to shear (i.e. proportional to</span>
<span id="L1881">                                ! |S|*tke). The values found by Jackson et al. are 0.14-0.12.</span>
<span id="L1882">KAPPA_BUOY_SCALE_COEF = 0.82    !   [nondim] default = 0.82</span>
<span id="L1883">                                ! The coefficient for the buoyancy length scale in the kappa equation.  The</span>
<span id="L1884">                                ! values found by Jackson et al. are in the range of 0.81-0.86.</span>
<span id="L1885">KAPPA_N_OVER_S_SCALE_COEF2 = 0.0 !   [nondim] default = 0.0</span>
<span id="L1886">                                ! The square of the ratio of the coefficients of the buoyancy and shear scales</span>
<span id="L1887">                                ! in the diffusivity equation, Set this to 0 (the default) to eliminate the</span>
<span id="L1888">                                ! shear scale. This is only used if USE_JACKSON_PARAM is true.</span>
<span id="L1889">LZ_RESCALE = 1.0                !   [nondim] default = 1.0</span>
<span id="L1890">                                ! A coefficient to rescale the distance to the nearest solid boundary. This</span>
<span id="L1891">                                ! adjustment is to account for regions where 3 dimensional turbulence prevents</span>
<span id="L1892">                                ! the growth of shear instabilies [nondim].</span>
<span id="L1893">KAPPA_SHEAR_TOL_ERR = 0.1       !   [nondim] default = 0.1</span>
<span id="L1894">                                ! The fractional error in kappa that is tolerated. Iteration stops when changes</span>
<span id="L1895">                                ! between subsequent iterations are smaller than this everywhere in a column.</span>
<span id="L1896">                                ! The peak diffusivities usually converge most rapidly, and have much smaller</span>
<span id="L1897">                                ! errors than this.</span>
<span id="L1898">TKE_BACKGROUND = 0.0            !   [m2 s-2] default = 0.0</span>
<span id="L1899">                                ! A background level of TKE used in the first iteration of the kappa equation.</span>
<span id="L1900">                                ! TKE_BACKGROUND could be 0.</span>
<span id="L1901">KAPPA_SHEAR_ELIM_MASSLESS = True !   [Boolean] default = True</span>
<span id="L1902">                                ! If true, massless layers are merged with neighboring massive layers in this</span>
<span id="L1903">                                ! calculation.  The default is true and I can think of no good reason why it</span>
<span id="L1904">                                ! should be false. This is only used if USE_JACKSON_PARAM is true.</span>
<span id="L1905">MAX_KAPPA_SHEAR_IT = 13         ! default = 13</span>
<span id="L1906">                                ! The maximum number of iterations that may be used to estimate the</span>
<span id="L1907">                                ! time-averaged diffusivity.</span>
<span id="L1908">PRANDTL_TURB = 1.0              !   [nondim] default = 1.0</span>
<span id="L1909">                                ! The turbulent Prandtl number applied to shear instability.</span>
<span id="L1910">KAPPA_SHEAR_MAX_KAP_SRC_CHG = 10.0 !   [nondim] default = 10.0</span>
<span id="L1911">                                ! The maximum permitted increase in the kappa source within an iteration</span>
<span id="L1912">                                ! relative to the local source; this must be greater than 1.  The lower limit</span>
<span id="L1913">                                ! for the permitted fractional decrease is (1 - 0.5/kappa_src_max_chg).  These</span>
<span id="L1914">                                ! limits could perhaps be made dynamic with an improved iterative solver.</span>
<span id="L1915">KAPPA_SHEAR_ITER_BUG = False    !   [Boolean] default = False</span>
<span id="L1916">                                ! If true, use an older, dimensionally inconsistent estimate of the derivative</span>
<span id="L1917">                                ! of diffusivity with energy in the Newton&#x27;s method iteration.  The bug causes</span>
<span id="L1918">                                ! undercorrections when dz &gt; 1 m.</span>
<span id="L1919">KAPPA_SHEAR_ALL_LAYER_TKE_BUG = False !   [Boolean] default = False</span>
<span id="L1920">                                ! If true, report back the latest estimate of TKE instead of the time average</span>
<span id="L1921">                                ! TKE when there is mass in all layers.  Otherwise always report the time</span>
<span id="L1922">                                ! averaged TKE, as is currently done when there are some massless layers.</span>
<span id="L1923">USE_RESTRICTIVE_TOLERANCE_CHECK = False !   [Boolean] default = False</span>
<span id="L1924">                                ! If true, uses the more restrictive tolerance check to determine if a timestep</span>
<span id="L1925">                                ! is acceptable for the KS_it outer iteration loop.  False uses the original</span>
<span id="L1926">                                ! less restrictive check.</span>
<span id="L1927"></span>
<span id="L1928">! === module MOM_CVMix_shear ===</span>
<span id="L1929">! Parameterization of shear-driven turbulence via CVMix (various options)</span>
<span id="L1930">USE_LMD94 = False               !   [Boolean] default = False</span>
<span id="L1931">                                ! If true, use the Large-McWilliams-Doney (JGR 1994) shear mixing</span>
<span id="L1932">                                ! parameterization.</span>
<span id="L1933">USE_PP81 = False                !   [Boolean] default = False</span>
<span id="L1934">                                ! If true, use the Pacanowski and Philander (JPO 1981) shear mixing</span>
<span id="L1935">                                ! parameterization.</span>
<span id="L1936"></span>
<span id="L1937">! === module MOM_CVMix_ddiff ===</span>
<span id="L1938">! Parameterization of mixing due to double diffusion processes via CVMix</span>
<span id="L1939">USE_CVMIX_DDIFF = False         !   [Boolean] default = False</span>
<span id="L1940">                                ! If true, turns on double diffusive processes via CVMix. Note that double</span>
<span id="L1941">                                ! diffusive processes on viscosity are ignored in CVMix, see</span>
<span id="L1942">                                ! http://cvmix.github.io/ for justification.</span>
<span id="L1943"></span>
<span id="L1944">! === module MOM_diabatic_aux ===</span>
<span id="L1945">! The following parameters are used for auxiliary diabatic processes.</span>
<span id="L1946">RECLAIM_FRAZIL = True           !   [Boolean] default = True</span>
<span id="L1947">                                ! If true, try to use any frazil heat deficit to cool any overlying layers down</span>
<span id="L1948">                                ! to the freezing point, thereby avoiding the creation of thin ice when the SST</span>
<span id="L1949">                                ! is above the freezing point.</span>
<span id="L1950">SALT_EXTRACTION_LIMIT = 0.9999  !   [nondim] default = 0.9999</span>
<span id="L1951">                                ! An upper limit on the fraction of the salt in a layer that can be lost to the</span>
<span id="L1952">                                ! net surface salt fluxes within a timestep.</span>
<span id="L1953">PRESSURE_DEPENDENT_FRAZIL = False !   [Boolean] default = False</span>
<span id="L1954">                                ! If true, use a pressure dependent freezing temperature when making frazil. The</span>
<span id="L1955">                                ! default is false, which will be faster but is inappropriate with ice-shelf</span>
<span id="L1956">                                ! cavities.</span>
<span id="L1957">IGNORE_FLUXES_OVER_LAND = False !   [Boolean] default = False</span>
<span id="L1958">                                ! If true, the model does not check if fluxes are being applied over land</span>
<span id="L1959">                                ! points. This is needed when the ocean is coupled with ice shelves and sea ice,</span>
<span id="L1960">                                ! since the sea ice mask needs to be different than the ocean mask to avoid sea</span>
<span id="L1961">                                ! ice formation under ice shelves. This flag only works when use_ePBL = True.</span>
<span id="L1962">DO_RIVERMIX = False             !   [Boolean] default = False</span>
<span id="L1963">                                ! If true, apply additional mixing wherever there is runoff, so that it is mixed</span>
<span id="L1964">                                ! down to RIVERMIX_DEPTH if the ocean is that deep.</span>
<span id="L1965">USE_RIVER_HEAT_CONTENT = False  !   [Boolean] default = False</span>
<span id="L1966">                                ! If true, use the fluxes%runoff_Hflx field to set the heat carried by runoff,</span>
<span id="L1967">                                ! instead of using SST*CP*liq_runoff.</span>
<span id="L1968">USE_CALVING_HEAT_CONTENT = False !   [Boolean] default = False</span>
<span id="L1969">                                ! If true, use the fluxes%calving_Hflx field to set the heat carried by runoff,</span>
<span id="L1970">                                ! instead of using SST*CP*froz_runoff.</span>
<span id="L1971">DO_BRINE_PLUME = False          !   [Boolean] default = False</span>
<span id="L1972">                                ! If true, use a brine plume parameterization from Nguyen et al., 2009.</span>
<span id="L1973">VAR_PEN_SW = False              !   [Boolean] default = False</span>
<span id="L1974">                                ! If true, use one of the CHL_A schemes specified by OPACITY_SCHEME to determine</span>
<span id="L1975">                                ! the e-folding depth of incoming short wave radiation.</span>
<span id="L1976"></span>
<span id="L1977">! === module MOM_energetic_PBL ===</span>
<span id="L1978">ML_OMEGA_FRAC = 0.0             !   [nondim] default = 0.0</span>
<span id="L1979">                                ! When setting the decay scale for turbulence, use this fraction of the absolute</span>
<span id="L1980">                                ! rotation rate blended with the local value of f, as sqrt((1-of)*f^2 +</span>
<span id="L1981">                                ! of*4*omega^2).</span>
<span id="L1982">EKMAN_SCALE_COEF = 1.0          !   [nondim] default = 1.0</span>
<span id="L1983">                                ! A nondimensional scaling factor controlling the inhibition of the diffusive</span>
<span id="L1984">                                ! length scale by rotation. Making this larger decreases the PBL diffusivity.</span>
<span id="L1985">EPBL_ANSWER_DATE = 99991231     ! default = 99991231</span>
<span id="L1986">                                ! The vintage of the order of arithmetic and expressions in the energetic PBL</span>
<span id="L1987">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1988">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1989">                                ! Values below 20240101 use A**(1./3.) to estimate the cube root of A in several</span>
<span id="L1990">                                ! expressions, while higher values use the integer root function cuberoot(A) and</span>
<span id="L1991">                                ! therefore can work with scaled variables.</span>
<span id="L1992">EPBL_ORIGINAL_PE_CALC = True    !   [Boolean] default = True</span>
<span id="L1993">                                ! If true, the ePBL code uses the original form of the potential energy change</span>
<span id="L1994">                                ! code.  Otherwise, the newer version that can work with successive increments</span>
<span id="L1995">                                ! to the diffusivity in upward or downward passes is used.</span>
<span id="L1996">MKE_TO_TKE_EFFIC = 0.0          !   [nondim] default = 0.0</span>
<span id="L1997">                                ! The efficiency with which mean kinetic energy released by mechanically forced</span>
<span id="L1998">                                ! entrainment of the mixed layer is converted to turbulent kinetic energy.</span>
<span id="L1999">TKE_DECAY = 2.5                 !   [nondim] default = 2.5</span>
<span id="L2000">                                ! TKE_DECAY relates the vertical rate of decay of the TKE available for</span>
<span id="L2001">                                ! mechanical entrainment to the natural Ekman depth.</span>
<span id="L2002">DIRECT_EPBL_MIXING_CALC = False !   [Boolean] default = False</span>
<span id="L2003">                                ! If true and there is no conversion from mean kinetic energy to ePBL turbulent</span>
<span id="L2004">                                ! kinetic energy, use a direct calculation of the diffusivity that is supported</span>
<span id="L2005">                                ! by a given energy input instead of the more general but slower iterative</span>
<span id="L2006">                                ! solver.</span>
<span id="L2007">EPBL_MSTAR_SCHEME = &quot;CONSTANT&quot;  ! default = &quot;CONSTANT&quot;</span>
<span id="L2008">                                ! EPBL_MSTAR_SCHEME selects the method for setting mstar.  Valid values are:</span>
<span id="L2009">                                !    CONSTANT   - Use a fixed mstar given by MSTAR</span>
<span id="L2010">                                !    OM4        - Use L_Ekman/L_Obukhov in the stabilizing limit, as in OM4</span>
<span id="L2011">                                !    REICHL_H18 - Use the scheme documented in Reichl &amp; Hallberg, 2018.</span>
<span id="L2012">MSTAR = 1.2                     !   [nondim] default = 1.2</span>
<span id="L2013">                                ! The ratio of the friction velocity cubed to the TKE input to the surface</span>
<span id="L2014">                                ! boundary layer.  This option is used if EPBL_MSTAR_SCHEME = CONSTANT.</span>
<span id="L2015">EPBL_BBL_USE_MSTAR = False      !   [nondim] default = False</span>
<span id="L2016">                                ! A logical to use mstar in the calculation of TKE in the ePBL BBL scheme</span>
<span id="L2017">NSTAR = 0.2                     !   [nondim] default = 0.2</span>
<span id="L2018">                                ! The portion of the buoyant potential energy imparted by surface fluxes that is</span>
<span id="L2019">                                ! available to drive entrainment at the base of mixed layer when that energy is</span>
<span id="L2020">                                ! positive.</span>
<span id="L2021">MSTAR_CONV_ADJ = 0.0            !   [nondim] default = 0.0</span>
<span id="L2022">                                ! Coefficient used for reducing mstar during convection due to reduction of</span>
<span id="L2023">                                ! stable density gradient.</span>
<span id="L2024">USE_MLD_ITERATION = False       !   [Boolean] default = True</span>
<span id="L2025">                                ! A logical that specifies whether or not to use the distance to the bottom of</span>
<span id="L2026">                                ! the actively turbulent boundary layer to help set the EPBL length scale.</span>
<span id="L2027">EPBL_TRANSITION_SCALE = 0.1     !   [nondim] default = 0.1</span>
<span id="L2028">                                ! A scale for the mixing length in the transition layer at the edge of the</span>
<span id="L2029">                                ! boundary layer as a fraction of the boundary layer thickness.</span>
<span id="L2030">EPBL_MIN_MIX_LEN = 0.0          !   [meter] default = 0.0</span>
<span id="L2031">                                ! The minimum mixing length scale that will be used by ePBL.  The default (0)</span>
<span id="L2032">                                ! does not set a minimum.</span>
<span id="L2033">MIX_LEN_EXPONENT = 2.0          !   [nondim] default = 2.0</span>
<span id="L2034">                                ! The exponent applied to the ratio of the distance to the MLD and the MLD depth</span>
<span id="L2035">                                ! which determines the shape of the mixing length. This is only used if</span>
<span id="L2036">                                ! USE_MLD_ITERATION is True.</span>
<span id="L2037">EPBL_VEL_SCALE_SCHEME = &quot;CUBE_ROOT_TKE&quot; ! default = &quot;CUBE_ROOT_TKE&quot;</span>
<span id="L2038">                                ! Selects the method for translating TKE into turbulent velocities. Valid values</span>
<span id="L2039">                                ! are:</span>
<span id="L2040">                                !    CUBE_ROOT_TKE  - A constant times the cube root of remaining TKE.</span>
<span id="L2041">                                !    REICHL_H18 - Use the scheme based on a combination of w* and v* as</span>
<span id="L2042">                                !                 documented in Reichl &amp; Hallberg, 2018.</span>
<span id="L2043">WSTAR_USTAR_COEF = 1.0          !   [nondim] default = 1.0</span>
<span id="L2044">                                ! A ratio relating the efficiency with which convectively released energy is</span>
<span id="L2045">                                ! converted to a turbulent velocity, relative to mechanically forced TKE. Making</span>
<span id="L2046">                                ! this larger increases the BL diffusivity</span>
<span id="L2047">EPBL_VEL_SCALE_FACTOR = 1.0     !   [nondim] default = 1.0</span>
<span id="L2048">                                ! An overall nondimensional scaling factor for wT. Making this larger increases</span>
<span id="L2049">                                ! the PBL diffusivity.</span>
<span id="L2050">VSTAR_SURF_FAC = 1.2            !   [nondim] default = 1.2</span>
<span id="L2051">                                ! The proportionality times ustar to set vstar at the surface.</span>
<span id="L2052">EPBL_BBL_EFFIC = 0.0            !   [nondim] default = 0.0</span>
<span id="L2053">                                ! The efficiency of bottom boundary layer mixing via ePBL.  Setting this to a</span>
<span id="L2054">                                ! value that is greater than 0 to enable bottom boundary layer mixing from EPBL.</span>
<span id="L2055">EPBL_BBL_TIDAL_EFFIC = 0.0      !   [nondim] default = 0.0</span>
<span id="L2056">                                ! The efficiency of bottom boundary layer mixing via ePBL driven by the bottom</span>
<span id="L2057">                                ! drag dissipation of tides, as provided in fluxes%BBL_tidal_dis.</span>
<span id="L2058">USE_LA_LI2016 = False           !   [Boolean] default = False</span>
<span id="L2059">                                ! A logical to use the Li et al. 2016 (submitted) formula to determine the</span>
<span id="L2060">                                ! Langmuir number.</span>
<span id="L2061">EPBL_LT = False                 !   [Boolean] default = False</span>
<span id="L2062">                                ! A logical to use a LT parameterization.</span>
<span id="L2063">EPBL_EQD_DIFFUSIVITY_SHAPE = False !   [nondim] default = False</span>
<span id="L2064">                                ! Logical flag for activating ML equation for shape function that uses forcing</span>
<span id="L2065">                                ! to change its structure.</span>
<span id="L2066">EPBL_EQD_DIFFUSIVITY_VELOCITY = False !   [nondim] default = False</span>
<span id="L2067">                                ! Logical flag for activating ML equation discovery for velocity scale</span>
<span id="L2068">EPBL_EQD_DIFFUSIVITY_VELOCITY_H = False !   [nondim] default = False</span>
<span id="L2069">                                ! Logical flag for activating ML equation discovery for velocity scale with h as</span>
<span id="L2070">                                ! input</span>
<span id="L2071">EPBL_OPTIONS_DIFF = 0           ! default = 0</span>
<span id="L2072">                                ! If positive, this is a coded integer indicating a pair of settings whose</span>
<span id="L2073">                                ! differences are diagnosed in a passive diagnostic mode  via extra calls to</span>
<span id="L2074">                                ! ePBL_column.  If this is 0 or negative no extra calls occur.</span>
<span id="L2075">!EPBL_USTAR_MIN = 1.45842E-23   !   [m s-1]</span>
<span id="L2076">                                ! The (tiny) minimum friction velocity used within the ePBL code, derived from</span>
<span id="L2077">                                ! OMEGA and ANGSTROM.</span>
<span id="L2078"></span>
<span id="L2079">! === module MOM_regularize_layers ===</span>
<span id="L2080">REGULARIZE_SURFACE_LAYERS = False !   [Boolean] default = False</span>
<span id="L2081">                                ! If defined, vertically restructure the near-surface layers when they have too</span>
<span id="L2082">                                ! much lateral variations to allow for sensible lateral barotropic transports.</span>
<span id="L2083"></span>
<span id="L2084">! === module MOM_opacity ===</span>
<span id="L2085">EXP_OPACITY_SCHEME = &quot;SINGLE_EXP&quot; ! default = &quot;SINGLE_EXP&quot;</span>
<span id="L2086">                                ! This character string specifies which exponential opacity scheme to utilize.</span>
<span id="L2087">                                ! Currently valid options include:</span>
<span id="L2088">                                !        SINGLE_EXP - Single Exponent decay.</span>
<span id="L2089">                                !        DOUBLE_EXP - Double Exponent decay.</span>
<span id="L2090">PEN_SW_SCALE = 15.0             !   [m] default = 0.0</span>
<span id="L2091">                                ! The vertical absorption e-folding depth of the penetrating shortwave</span>
<span id="L2092">                                ! radiation.</span>
<span id="L2093">PEN_SW_FRAC = 0.42              !   [nondim] default = 0.0</span>
<span id="L2094">                                ! The fraction of the shortwave radiation that penetrates below the surface.</span>
<span id="L2095">PEN_SW_NBANDS = 1               ! default = 1</span>
<span id="L2096">                                ! The number of bands of penetrating shortwave radiation.</span>
<span id="L2097">OPTICS_ANSWER_DATE = 99991231   ! default = 99991231</span>
<span id="L2098">                                ! The vintage of the order of arithmetic and expressions in the optics</span>
<span id="L2099">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L2100">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L2101">PEN_SW_FLUX_ABSORB = 2.5E-11    !   [degC m s-1] default = 2.5E-11</span>
<span id="L2102">                                ! A minimum remaining shortwave heating rate that will be simply absorbed in the</span>
<span id="L2103">                                ! next sufficiently thick layers for computational efficiency, instead of</span>
<span id="L2104">                                ! continuing to penetrate.  The default, 2.5e-11 degC m s-1, is about 1e-4 W m-2</span>
<span id="L2105">                                ! or 0.08 degC m century-1, but 0 is also a valid value.</span>
<span id="L2106">PEN_SW_ABSORB_MINTHICK = 1.0    !   [m] default = 1.0</span>
<span id="L2107">                                ! A thickness that is used to absorb the remaining penetrating shortwave heat</span>
<span id="L2108">                                ! flux when it drops below PEN_SW_FLUX_ABSORB.</span>
<span id="L2109">OPACITY_LAND_VALUE = 10.0       !   [m-1] default = 10.0</span>
<span id="L2110">                                ! The value to use for opacity over land. The default is 10 m-1 - a value for</span>
<span id="L2111">                                ! muddy water.</span>
<span id="L2112"></span>
<span id="L2113">! === module MOM_tracer_advect ===</span>
<span id="L2114">TRACER_ADVECTION_SCHEME = &quot;PLM&quot; ! default = &quot;PLM&quot;</span>
<span id="L2115">                                ! The horizontal transport scheme for tracers:</span>
<span id="L2116">                                !   PLM    - Piecewise Linear Method</span>
<span id="L2117">                                !   PPM:H3 - Piecewise Parabolic Method (Huyhn 3rd order)</span>
<span id="L2118">                                !   PPM    - Piecewise Parabolic Method (Colella-Woodward)</span>
<span id="L2119"></span>
<span id="L2120">! === module MOM_tracer_hor_diff ===</span>
<span id="L2121">KHTR = 1.0                      !   [m2 s-1] default = 0.0</span>
<span id="L2122">                                ! The background along-isopycnal tracer diffusivity.</span>
<span id="L2123">KHTR_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L2124">                                ! The minimum along-isopycnal tracer diffusivity.</span>
<span id="L2125">KHTR_MAX = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L2126">                                ! The maximum along-isopycnal tracer diffusivity. Set to a positive value to</span>
<span id="L2127">                                ! activate.</span>
<span id="L2128">KHTR_PASSIVITY_COEFF = 0.0      !   [nondim] default = 0.0</span>
<span id="L2129">                                ! The coefficient that scales deformation radius over grid-spacing in passivity,</span>
<span id="L2130">                                ! where passivity is the ratio between along isopycnal mixing of tracers to</span>
<span id="L2131">                                ! thickness mixing. A non-zero value enables this parameterization.</span>
<span id="L2132">KHTR_PASSIVITY_MIN = 0.5        !   [nondim] default = 0.5</span>
<span id="L2133">                                ! The minimum passivity which is the ratio between along isopycnal mixing of</span>
<span id="L2134">                                ! tracers to thickness mixing.</span>
<span id="L2135">DIFFUSE_ML_TO_INTERIOR = False  !   [Boolean] default = False</span>
<span id="L2136">                                ! If true, enable epipycnal mixing between the surface boundary layer and the</span>
<span id="L2137">                                ! interior.</span>
<span id="L2138">CHECK_DIFFUSIVE_CFL = False     !   [Boolean] default = False</span>
<span id="L2139">                                ! If true, use enough iterations the diffusion to ensure that the diffusive</span>
<span id="L2140">                                ! equivalent of the CFL limit is not violated.  If false, always use the greater</span>
<span id="L2141">                                ! of 1 or MAX_TR_DIFFUSION_CFL iteration.</span>
<span id="L2142">MAX_TR_DIFFUSION_CFL = -1.0     !   [nondim] default = -1.0</span>
<span id="L2143">                                ! If positive, locally limit the along-isopycnal tracer diffusivity to keep the</span>
<span id="L2144">                                ! diffusive CFL locally at or below this value.  The number of diffusive</span>
<span id="L2145">                                ! iterations is often this value or the next greater integer.</span>
<span id="L2146">RECALC_NEUTRAL_SURF = False     !   [Boolean] default = False</span>
<span id="L2147">                                ! If true, then recalculate the neutral surfaces if the</span>
<span id="L2148">                                ! diffusive CFL is exceeded. If false, assume that the</span>
<span id="L2149">                                ! positions of the surfaces do not change</span>
<span id="L2150"></span>
<span id="L2151">! === module MOM_neutral_diffusion ===</span>
<span id="L2152">! This module implements neutral diffusion of tracers</span>
<span id="L2153">USE_NEUTRAL_DIFFUSION = False   !   [Boolean] default = False</span>
<span id="L2154">                                ! If true, enables the neutral diffusion module.</span>
<span id="L2155"></span>
<span id="L2156">! === module MOM_hor_bnd_diffusion ===</span>
<span id="L2157">! This module implements horizontal diffusion of tracers near boundaries</span>
<span id="L2158">USE_HORIZONTAL_BOUNDARY_DIFFUSION = False !   [Boolean] default = False</span>
<span id="L2159">                                ! If true, enables the horizonal boundary tracer&#x27;s diffusion module.</span>
<span id="L2160">OBSOLETE_DIAGNOSTIC_IS_FATAL = True !   [Boolean] default = True</span>
<span id="L2161">                                ! If an obsolete diagnostic variable appears in the diag_table, cause a FATAL</span>
<span id="L2162">                                ! error rather than issue a WARNING.</span>
<span id="L2163"></span>
<span id="L2164">! === module MOM_sum_output ===</span>
<span id="L2165">CALCULATE_APE = False           !   [Boolean] default = True</span>
<span id="L2166">                                ! If true, calculate the available potential energy of the interfaces.  Setting</span>
<span id="L2167">                                ! this to false reduces the memory footprint of high-PE-count models</span>
<span id="L2168">                                ! dramatically.</span>
<span id="L2169">WRITE_STOCKS = True             !   [Boolean] default = True</span>
<span id="L2170">                                ! If true, write the integrated tracer amounts to stdout when the energy files</span>
<span id="L2171">                                ! are written.</span>
<span id="L2172">MAXTRUNC = 5000                 !   [truncations save_interval-1] default = 0</span>
<span id="L2173">                                ! The run will be stopped, and the day set to a very large value if the velocity</span>
<span id="L2174">                                ! is truncated more than MAXTRUNC times between energy saves.  Set MAXTRUNC to 0</span>
<span id="L2175">                                ! to stop if there is any truncation of velocities.</span>
<span id="L2176">MAX_ENERGY = 0.0                !   [m2 s-2] default = 0.0</span>
<span id="L2177">                                ! The maximum permitted average energy per unit mass; the model will be stopped</span>
<span id="L2178">                                ! if there is more energy than this.  If zero or negative, this is set to</span>
<span id="L2179">                                ! 10*MAXVEL^2.</span>
<span id="L2180">MAXVEL = 10.0                   !   [m s-1] default = 3.0E+08</span>
<span id="L2181">                                ! The maximum velocity allowed before the velocity components are truncated.</span>
<span id="L2182">ENERGYFILE = &quot;ocean.stats&quot;      ! default = &quot;ocean.stats&quot;</span>
<span id="L2183">                                ! The file to use to write the energies and globally summed diagnostics.</span>
<span id="L2184">DATE_STAMPED_STDOUT = False     !   [Boolean] default = True</span>
<span id="L2185">                                ! If true, use dates (not times) in messages to stdout</span>
<span id="L2186">ISO_DATE_STAMPED_STDOUT = False !   [Boolean] default = False</span>
<span id="L2187">                                ! If true, use ISO formatted dates in messages to stdout</span>
<span id="L2188">TIMEUNIT = 8.64E+04             !   [s] default = 8.64E+04</span>
<span id="L2189">                                ! The time unit in seconds a number of input fields</span>
<span id="L2190">ENERGYSAVEDAYS = 0.125          !   [days] default = 1.0</span>
<span id="L2191">                                ! The interval in units of TIMEUNIT between saves of the energies of the run and</span>
<span id="L2192">                                ! other globally summed diagnostics.</span>
<span id="L2193">ENERGYSAVEDAYS_GEOMETRIC = 0.0  !   [days] default = 0.0</span>
<span id="L2194">                                ! The starting interval in units of TIMEUNIT for the first call to save the</span>
<span id="L2195">                                ! energies of the run and other globally summed diagnostics. The interval</span>
<span id="L2196">                                ! increases by a factor of 2. after each call to write_energy.</span>
<span id="L2197"></span>
<span id="L2198">! === module ocean_stochastics_init ===</span>
<span id="L2199">DO_SPPT = False                 !   [Boolean] default = False</span>
<span id="L2200">                                ! If true, then stochastically perturb the thermodynamic tendencies of T,S, amd</span>
<span id="L2201">                                ! h.  Amplitude and correlations are controlled by the nam_stoch namelist in the</span>
<span id="L2202">                                ! UFS model only.</span>
<span id="L2203">DO_SKEB = False                 !   [Boolean] default = False</span>
<span id="L2204">                                ! If true, then stochastically perturb the currents using the stochastic kinetic</span>
<span id="L2205">                                ! energy backscatter scheme.</span>
<span id="L2206">PERT_EPBL = False               !   [Boolean] default = False</span>
<span id="L2207">                                ! If true, then stochastically perturb the kinetic energy production and</span>
<span id="L2208">                                ! dissipation terms.  Amplitude and correlations are controlled by the nam_stoch</span>
<span id="L2209">                                ! namelist in the UFS model only.</span>
<span id="L2210">INITIALIZE_ICE_SHEET_SMB = False !   [Boolean] default = False</span>
<span id="L2211">                                ! Read in a constant SMB for the ice sheet</span>
<span id="L2212"></span>
<span id="L2213">! === module MOM_surface_forcing ===</span>
<span id="L2214">VARIABLE_WINDS = False          !   [Boolean] default = True</span>
<span id="L2215">                                ! If true, the winds vary in time after the initialization.</span>
<span id="L2216">VARIABLE_BUOYFORCE = False      !   [Boolean] default = True</span>
<span id="L2217">                                ! If true, the buoyancy forcing varies in time after the initialization of the</span>
<span id="L2218">                                ! model.</span>
<span id="L2219">BUOY_CONFIG = &quot;NONE&quot;            ! default = &quot;zero&quot;</span>
<span id="L2220">                                ! The character string that indicates how buoyancy forcing is specified.  Valid</span>
<span id="L2221">                                ! options include (file), (data_override), (zero), (const), (linear), (MESO),</span>
<span id="L2222">                                ! (SCM_CVmix_tests), (BFB), (dumbbell), (USER) and (NONE).</span>
<span id="L2223">WIND_CONFIG = &quot;zero&quot;            ! default = &quot;zero&quot;</span>
<span id="L2224">                                ! The character string that indicates how wind forcing is specified.  Valid</span>
<span id="L2225">                                ! options include (file), (data_override), (2gyre), (1gyre), (gyres), (zero),</span>
<span id="L2226">                                ! (const), (Neverworld), (scurves), (ideal_hurr), (SCM_CVmix_tests) and (USER).</span>
<span id="L2227">RESTOREBUOY = False             !   [Boolean] default = False</span>
<span id="L2228">                                ! If true, the buoyancy fluxes drive the model back toward some specified</span>
<span id="L2229">                                ! surface state with a rate given by FLUXCONST.</span>
<span id="L2230">LATENT_HEAT_VAPORIZATION = 2.5E+06 !   [J/kg] default = 2.5E+06</span>
<span id="L2231">                                ! The latent heat of fusion.</span>
<span id="L2232">GUST_CONST = 0.02               !   [Pa] default = 0.0</span>
<span id="L2233">                                ! The background gustiness in the winds.</span>
<span id="L2234">USTAR_GUSTLESS_BUG = False      !   [Boolean] default = False</span>
<span id="L2235">                                ! If true include a bug in the time-averaging of the gustless wind friction</span>
<span id="L2236">                                ! velocity</span>
<span id="L2237">READ_GUST_2D = False            !   [Boolean] default = False</span>
<span id="L2238">                                ! If true, use a 2-dimensional gustiness supplied from an input file</span>
<span id="L2239"></span>
<span id="L2240">! === module MOM_restart ===</span>
<span id="L2241">USE_WAVES = False               !   [Boolean] default = False</span>
<span id="L2242">                                ! If true, enables surface wave modules.</span>
<span id="L2243"></span>
<span id="L2244">! === module MOM_main (MOM_driver) ===</span>
<span id="L2245">DAYMAX = 90.0                   !   [days]</span>
<span id="L2246">                                ! The final time of the whole simulation, in units of TIMEUNIT seconds.  This</span>
<span id="L2247">                                ! also sets the potential end time of the present run segment if the end time is</span>
<span id="L2248">                                ! not set via ocean_solo_nml in input.nml.</span>
<span id="L2249">SINGLE_STEPPING_CALL = True     !   [Boolean] default = True</span>
<span id="L2250">                                ! If true, advance the state of MOM with a single step including both dynamics</span>
<span id="L2251">                                ! and thermodynamics.  If false the two phases are advanced with separate calls.</span>
<span id="L2252">RESTART_CONTROL = 1             ! default = 1</span>
<span id="L2253">                                ! An integer whose bits encode which restart files are written. Add 2 (bit 1)</span>
<span id="L2254">                                ! for a time-stamped file, and odd (bit 0) for a non-time-stamped file. A</span>
<span id="L2255">                                ! non-time-stamped restart file is saved at the end of the run segment for any</span>
<span id="L2256">                                ! non-negative value.</span>
<span id="L2257">RESTINT = 0.0                   !   [days] default = 0.0</span>
<span id="L2258">                                ! The interval between saves of the restart file in units of TIMEUNIT.  Use 0</span>
<span id="L2259">                                ! (the default) to not save incremental restart files at all.</span>
<span id="L2260">WRITE_CPU_STEPS = 1000          ! default = 1000</span>
<span id="L2261">                                ! The number of coupled timesteps between writing the cpu time. If this is not</span>
<span id="L2262">                                ! positive, do not check cpu time, and the segment run-length can not be set via</span>
<span id="L2263">                                ! an elapsed CPU time.</span>
<span id="L2264"></span>
<span id="L2265">! === module MOM_write_cputime ===</span>
<span id="L2266">MAXCPU = 2.88E+04               !   [wall-clock seconds] default = -1.0</span>
<span id="L2267">                                ! The maximum amount of cpu time per processor for which MOM should run before</span>
<span id="L2268">                                ! saving a restart file and quitting with a return value that indicates that a</span>
<span id="L2269">                                ! further run is required to complete the simulation. If automatic restarts are</span>
<span id="L2270">                                ! not desired, use a negative value for MAXCPU.  MAXCPU has units of wall-clock</span>
<span id="L2271">                                ! seconds, so the actual CPU time used is larger by a factor of the number of</span>
<span id="L2272">                                ! processors used.</span>
<span id="L2273">CPU_TIME_FILE = &quot;CPU_stats&quot;     ! default = &quot;CPU_stats&quot;</span>
<span id="L2274">                                ! The file into which CPU time is written.</span>
<span id="L2275"></span>
<span id="L2276">! === module MOM_file_parser ===</span>
<span id="L2277">SEND_LOG_TO_STDOUT = False      !   [Boolean] default = False</span>
<span id="L2278">                                ! If true, all log messages are also sent to stdout.</span>
<span id="L2279">DOCUMENT_FILE = &quot;MOM_parameter_doc&quot; ! default = &quot;MOM_parameter_doc&quot;</span>
<span id="L2280">                                ! The basename for files where run-time parameters, their settings, units and</span>
<span id="L2281">                                ! defaults are documented. Blank will disable all parameter documentation.</span>
<span id="L2282">COMPLETE_DOCUMENTATION = True   !   [Boolean] default = True</span>
<span id="L2283">                                ! If true, all run-time parameters are documented in MOM_parameter_doc.all .</span>
<span id="L2284">MINIMAL_DOCUMENTATION = True    !   [Boolean] default = True</span>
<span id="L2285">                                ! If true, non-default run-time parameters are documented in</span>
<span id="L2286">                                ! MOM_parameter_doc.short .</span>
</pre>
